"""
From a list of domains remove those which not follow rules"""

import pandas as pd

DIRECTORY = "data/"
FILENAME = 'DomainsRegistered2018-03-01.txt'
FILTER_CHARS = '^[a-zA-Z-\.]+$'
FILTER_CONSOMNANTS = '^[bcdfghjklmnpqrstvwxyz]{4}'
DATA = pd.read_csv(DIRECTORY+FILENAME, names=["url"])
print len(DATA.index)

# Remove domains with numbers,shorter than 10 chars and with consomnant long sequences
DATA_NO_NUMBERS = DATA[DATA.url.str.contains(FILTER_CHARS)]
print len(DATA_NO_NUMBERS.index)

DNNNR = DATA_NO_NUMBERS[~DATA_NO_NUMBERS.url.str.contains(FILTER_CONSOMNANTS)]
print len(DNNNR.index)

NEW_DATA = DNNNR
NEW_DATA = NEW_DATA[NEW_DATA .url.str.len() > 10]
print len(NEW_DATA.index)

LIST_URLS = NEW_DATA['url'].apply(lambda x: "http://www." + x)
LIST_URLS.to_csv(DIRECTORY + "Clean" + FILENAME, index=False, header=False)
