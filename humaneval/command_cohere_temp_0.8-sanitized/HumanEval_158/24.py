def find_max(words):
    char_count = {}
    max_count = 0
    max_word = None

    for word in words:
        unique_chars = set(word)
        count = len(unique_chars)
        if count > max_count:
            max_count = count
            max_word = word
        if count == max_count:
            if word < max_word:
                max_word = word

    return max_word