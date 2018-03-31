import requests
import re
import os
from collections import Counter

TRAINING_TXT_URL = "https://norvig.com/big.txt"
CACHE_FILE = "files/cache.txt"
WORDS_RE = r"[a-z]+"


def cache(f, file=CACHE_FILE):
    def _cache(*args, **kwargs):
        if os.path.isfile(CACHE_FILE):
            return open(CACHE_FILE).read()
        res = f(*args, **kwargs)
        open(CACHE_FILE, 'w').write(res)
        return res
    return _cache


@cache
def get_training_txt(url):
    res = requests.get(url, stream=True)
    res.raise_for_status()
    return res.text


def words_in_file(text):
    return re.findall(WORDS_RE, text.lower())


def word_frequency(text):
    words = words_in_file(text)
    return Counter(words)


text = get_training_txt(TRAINING_TXT_URL)
# cache_text(text)
words = words_in_file(text)
freq = Counter(words)
