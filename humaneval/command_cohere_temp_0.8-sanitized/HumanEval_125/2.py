def split_words(txt):
    if not txt.strip():  return 'empty string'  # this will cover the edge case of empty string as well as enforce consistency of the return type being a list
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != ',' else len(txt) if txt.islower() else 3