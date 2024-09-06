def find_max(words):
    max_char_word = None
    char_count = 0

    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > char_count:
            max_char_word = word
            char_count = len(unique_chars)

    return max_char_word