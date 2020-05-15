import pytest
from music_metadata_extractor import SongData


def test_youtube_clean_title():
    song_data = SongData("https://youtu.be/RfT-BpC2cPo")
    assert song_data is not None

    track = song_data.track
    artists = song_data.artists
    assert track.name == "It Follows"
    assert artists[0].name == "Pencey Sloe"


def test_youtube_almost_clean_title():
    song_data = SongData("https://www.youtube.com/watch?v=XoYu7K6Ywkg")
    assert song_data is not None

    track = song_data.track
    artists = song_data.artists
    assert track.name == "Last Hope"
    assert artists[0].name == "Paramore"


def test_youtube_embed_url():
    song_data = SongData("https://www.youtube.com/embed/HkwCtYVv3QQ?autoplay=1")
    assert song_data is not None


def test_spotify():
    with pytest.raises(ValueError) as ex:
        song_data = SongData("https://open.spotify.com/track/7w6QlKAOcNEnqRgrnJvQtr")
    assert str(ex.value) == "Unsupported URL!"
