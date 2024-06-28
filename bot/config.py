import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("7209573172:AAGTNEZaVVe5Jw5uZed9LsgJsvjn-vyZHCs", None)
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('b23507de0081e14e3f32d5cca6ce09a8')
    TELEGRAM_APP_ID=int(getenv('23805382'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
