def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != [''] else len(set(txt.lower())) % 2 == 1