def find_max(words):
    max_uniq_char_word = None
    max_uniq_char_count = 0

    for word in words:
        unique_characters = set(word)
        uniq_char_count = len(unique_characters)

        if uniq_char_count > max_uniq_char_count:
            max_uniq_char_count = uniq_char_count
            max_uniq_char_word = word

    return max_uniq_char_word