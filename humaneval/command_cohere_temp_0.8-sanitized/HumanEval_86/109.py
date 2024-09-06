def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True

    for c in s:
        if not blank_start and c.isspace():
            if word_arr:
                word_start = True
        elif blank_start or (c.isspace() and word_start):
            blank_start = False
            word_start = False
            word_arr.append(c)
        else:
            if 96 <= c <= 123:
                blank_start = False
                word_start = False
                word_arr.append(c)
            else:
                if not (blank_start or word_start):
                    word_arr.append('')
        # print(c, blank_start, word_start, word_arr)

    # Added sentinel at the end to avoid extra space
    return ' '.join(word_arr + ['~'])