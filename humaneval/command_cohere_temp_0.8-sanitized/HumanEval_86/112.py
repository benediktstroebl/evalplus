def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        char_array = list(word)
        char_array.sort()
        new_word = ''.join(char_array)
        new_word_array.append(new_word)

    return ' '.join(new_word_array)