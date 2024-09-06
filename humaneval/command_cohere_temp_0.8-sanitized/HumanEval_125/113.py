def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return words