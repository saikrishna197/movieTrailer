"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""

    Baahubali_2 = media.Movie("Baahubali 2: The Conclusion",
                              "Starts off as an ace warrior only to"
                              "be tamed into someone who has to be protected",
                              "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=qD-6d8Wo3do",
                              "April 28, 2017")

    res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw",
                           "March 15, 2002")

    matrix = media.Movie("The Matrix",
                         "The world is a simulation",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "March 31, 1999")
    # Store the Movie objects in a list.
    movies = [Baahubali_2, res_evil, matrix]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
