import os
import pandas as pd
import requests


class GameDataAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.rawg.io/api/games'
        self.params = {
            'key': self.api_key,
            'page_size': 40,
            'dates': '1980-01-01,2023-12-31'
        }
        self.create_directories()

    def create_directories(self):
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists('data/arff'):
            os.makedirs('data/arff')

    def fetch_data(self):
        games_data = pd.DataFrame(columns=['name', 'genre', 'released', 'rating'])
        while True:
            response = requests.get(self.url, params=self.params)
            if response.status_code != 200:
                break
            data = response.json()
            temp_data = []
            for game in data['results']:
                for genre in game['genres']:
                    row = {
                        'name': game['name'],
                        'genre': genre['name'],
                        'released': game['released'],
                        'rating': game['rating']
                    }
                    temp_data.append(row)
            games_data = pd.concat([games_data, pd.DataFrame(temp_data)], ignore_index=True)
            if 'next' in data and data['next']:
                self.url = data['next']
            else:
                break
        games_data.to_csv('data/games_data_with_ratings.csv', index=False)

    def process_data(self):
        games_data = pd.read_csv('data/games_data_with_ratings.csv')
        games_data['released'] = pd.to_datetime(games_data['released'], errors='coerce')
        games_data['year'] = games_data['released'].dt.year
        games_data['rating'] = pd.to_numeric(games_data['rating'], errors='coerce')

        success_threshold = 3.2
        average_ratings_count = games_data.groupby(['genre', 'year']).agg(
            average_rating=('rating', 'mean'),
            game_count=('rating', 'count')
        ).reset_index()
        average_ratings_count['genre_successful'] = average_ratings_count['average_rating'].apply(
            lambda x: 1 if x >= success_threshold else 0)

        average_ratings_count.to_csv('data/average_ratings_count_success_by_genre_and_year.csv', index=False)
        print("Results saved: 'data/average_ratings_count_success_by_genre_and_year.csv'")

    def convert_csv_to_arff(self, csv_file, arff_file):
        data = pd.read_csv(csv_file)

        with open(arff_file, 'w') as f:
            f.write('@RELATION video_games\n\n')
            for column in data.columns:
                if data[column].dtype == object:
                    f.write(f"@ATTRIBUTE {column} STRING\n")
                else:
                    f.write(f"@ATTRIBUTE {column} NUMERIC\n")

            f.write('\n@DATA\n')
            for index, row in data.iterrows():
                row_str = ','.join(str(value) for value in row)
                f.write(row_str + '\n')

        print(f"ARFF file saved as {arff_file}")


api_key = 'your_api_key'
analyzer = GameDataAnalyzer(api_key)
analyzer.fetch_data()
analyzer.process_data()
analyzer.convert_csv_to_arff('data/average_ratings_count_success_by_genre_and_year.csv', 'data/arff/video_games_data.arff')

