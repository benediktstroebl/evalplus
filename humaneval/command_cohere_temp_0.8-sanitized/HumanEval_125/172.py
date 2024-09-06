def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split(' ')
    return words if words != ')' else len(words) if words == '(' else [word for word in words if word != '']