def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        char_set = set(word)
        if char_set not in max_set or (char_set == max_set and word < max_word):
            max_set = char_set
            max_word = word
    return max_word