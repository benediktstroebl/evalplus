def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        unique = set(word)
        if not max_set or len(unique) > len(max_set):
            max_set = unique
            max_word = word
    return max_word