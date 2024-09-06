def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        new_word = ''.join(sorted(word))
        new_word_list.append(new_word)
    return ' '.join(new_word_list)