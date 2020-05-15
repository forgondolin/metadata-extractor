import requests
from bs4 import BeautifulSoup
from .helpers import cleanse
from .scraper import scrape_embedded_yt_metadata, scrape_yt
from music_metadata_extractor.models import BaseProviderInput


def get_info(url: str) -> BaseProviderInput:
    """Generate provider input object for YouTube URL"""
    clean_url = cleanse(url)
    response = requests.get(clean_url)
    soup = BeautifulSoup(response.content, "lxml")

    return scrape_yt(soup)
