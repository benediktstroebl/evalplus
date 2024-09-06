def split_words(txt):
    if txt.find(' ') != -1 or txt.find(',') != -1:
        words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    else:
        words = len(list(filter(lambda x: x in str.lower(), txt)))
    return words