"""Download weather data from the configured API."""

import requests

from .config import URL, TIMEOUT


class WeatherDownloadError(Exception):
    """Represent a failed weather download."""


class WeatherSource:
    """Retrieve weather JSON from an API."""

    def __init__(self, url=URL, timeout=TIMEOUT):
        self.url = url
        self.timeout = timeout

    def download(self):
        try:
            response = requests.get(
                self.url,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException as error:
            raise WeatherDownloadError(
                f"Weather download failed: {error}"
            ) from error