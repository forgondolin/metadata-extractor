import re


def cleanse(url: str) -> str:
    pattern_match = re.search(
        (
            r"(?:https?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/"
            r"(?:watch|v|embed)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\-_]+)"
        ),
        url,
    )
    video_id = pattern_match.group(1)
    clean_url = "https://www.youtube.com/watch?v=%s" % (video_id)
    return clean_url


def clean_channel(raw_channel: str) -> str:
    """Clean channel name"""
    clean_channel = raw_channel
    dirt = ["-", "topic", "Topic"]
    for substr in dirt:
        clean_channel = clean_channel.replace(substr, "")
    return clean_channel.strip()


# To escape KeyError
def check_key_get_value(data, key):
    if key in data.keys():
        return data[key]
    return None
