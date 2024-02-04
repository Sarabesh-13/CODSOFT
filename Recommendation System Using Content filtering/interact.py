import pandas as pd

data = pd.read_csv("C:\\Users\\HP\\Downloads\\content filtering\\merged_dataset.csv")

def get_best_movies_interactive(data: pd.DataFrame, movie_column: str = 'Movie_Name', rating_column: str = 'Rating', num_movies: int = 5) -> pd.DataFrame:
    
    #Get a list of the best movies based on ratings in an interactive session.
    while True:
        try:
            user_input = input("Enter the number of top-rated movies to retrieve (or 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                break

            num_movies = int(user_input)

            if num_movies <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            continue

        # Sort the DataFrame by ratings in descending order
        sorted_df = data.sort_values(by=rating_column,ascending=False)

        # Get the top-rated movies
        best_movies = sorted_df.head(num_movies)

        if not best_movies.empty:
            print(f"\nTop {num_movies} movies based on ratings:\n", best_movies[[movie_column, rating_column]])
        else:
            print("No movies found in the dataset.")

# Call the function
get_best_movies_interactive(data)
