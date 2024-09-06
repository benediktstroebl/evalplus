def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)

    return ' '.join(new_word_array)