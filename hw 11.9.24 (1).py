# START

min_movie: int = int(input('Enter the movie time in minutes: '))
movie_h: int = min_movie // 60
movie_minute: int = min_movie % 60

if min_movie <= 0:
    print("you didn't watch the movie")
else:
    print(f"The movie is {movie_h} hour/s and {movie_minute} minutes!!! ")

# END
