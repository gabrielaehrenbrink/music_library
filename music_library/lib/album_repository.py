from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        """
        returns a list of album objects:
        No arguents
        """
        rows = self._connection.execute("SELECT * FROM albums")

        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * FROM albums WHERE id = %s", [artist_id]
        )
        record = rows[0]
        return Album(
            record["id"], record["title"], record["release_year"], record["artist_id"]
        )
