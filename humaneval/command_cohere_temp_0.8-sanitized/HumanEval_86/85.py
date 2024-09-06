def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not c.isspace():
            if not word_start:
                word_arr.append(c)
                word_start = True
            else:
                word_arr.append(c)
        else:
            if word_start:
                word_start = False
                blank_start = False
                word = ''.join(word_arr)
                word_arr.clear()
                word_arr.append(word)
            else:
                blank_start = False
    if word_start:
        word_arr.clear()
        word_arr.append(s)
    return ' '.join(word_arr)