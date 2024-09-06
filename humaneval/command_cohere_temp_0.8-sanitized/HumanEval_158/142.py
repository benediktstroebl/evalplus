def find_max(words):
    max_count = 0
    max_word = None
    for word in words:
        unique = set(word)
        count = len(unique)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word