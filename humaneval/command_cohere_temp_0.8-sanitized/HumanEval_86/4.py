def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not c.isspace():
            if not word_start:
                blank_start = False
                word_arr.append('')
            word_arr[-1] += c
        else:
            if not blank_start:
                word_start = True
                blank_start = True
                word_arr.append('')
            else:
                blank_start = False
    return ' '.join(word_arr)