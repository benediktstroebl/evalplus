def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not blank_start and not word_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif not blank_start and word_start and c.isspace():
            word_start = False
            word = ''.join(word_arr)
            s = s.replace(word, ''.join(sorted(word)))
            blank_start = False
            word_arr = []
        else:
            blank_start = False
            word_arr.append(c)
    return s