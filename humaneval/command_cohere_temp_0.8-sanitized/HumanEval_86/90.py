def anti_shuffle(s):
    word_arr = s.split()
    new_word_arr = []
    for word in word_arr:
        char_arr = list(word)
        char_arr.sort()
        new_word = ''.join(char_arr)
        new_word_arr.append(new_word)
    return ' '.join(new_word_arr)