def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not blank_start and not word_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif blank_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif not c.isalpha():
            if word_start:
                word_arr.sort()
                word_start = False
            blank_start = False
        else:
            blank_start = True
    if word_start:
        word_arr.sort()
    return ' '.join(word_arr)