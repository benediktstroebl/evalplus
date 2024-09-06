def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not c.isspace():
            if not word_start:
                word_arr.append(c)
                blank_start = False
                word_start = True
            else:
                word_arr.append(c)
        else:
            if not blank_start:
                word_start = False
                word_arr.append('')
                blank_start = True
            else:
                blank_start = False
    word_str = ''.join(word_arr)
    # Sorting based on ascii value
    sorted_word = ''.join(sorted(word_str))
    return ' '.join(s.split()[:len(word_arr) + len(s.split()) // 2]) + sorted_word + ' '.join(s.split()[-len(word_arr) - len(s.split()) // 2:])