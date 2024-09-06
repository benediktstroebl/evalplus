def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split(' ')
    return words if words != ',' else len(txt) if txt.islower() else 3