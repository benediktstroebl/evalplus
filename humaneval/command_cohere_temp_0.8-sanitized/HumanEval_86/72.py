def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        ascii_sorted = ''.join(sorted(word))
        new_word_list.append(ascii_sorted)
    return ' '.join(new_word_list)