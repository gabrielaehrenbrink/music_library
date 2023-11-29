# file: app.py

from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection


class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!

        while True:
            user_input = input(
                "What would you like to do?\n\t1 - List of albums\n\t2 - List of artists\n\nEnter your choice: "
            )
            if user_input in ["1", "2"]:
                break
            else:
                print("Please enter either 1 or 2\n")
                continue

        if user_input == "1":
            album_repo = AlbumRepository(self._connection)
            albums = album_repo.all()

            print("Here is a list of albums:\n")
            for album in albums:
                print(f"{album.id} - {album.title}")

        if user_input == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

            print("Here is a list of albums:\n")
            for artist in artists:
                print(f"{artist.id} - {artist.name}")


if __name__ == "__main__":
    app = Application()
    app.run()
