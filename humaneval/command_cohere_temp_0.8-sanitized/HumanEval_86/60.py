def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not c.isspace():
            if not word_start:
                word_arr.append(c)
                blank_start = False
            else:
                word_arr.append(c)
        else:
            if not blank_start:
                word_start = True
                word_arr.append('')
            else:
                blank_start = False
    word_arr.reverse()
    joined = ''.join(word_arr)
    return joined