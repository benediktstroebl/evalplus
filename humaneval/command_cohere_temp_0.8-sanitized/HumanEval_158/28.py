def find_max(words):
    max_uniq_char_word = None
    max_uniq_char_count = 0

    for word in words:
        unique_characters = set(word)
        current_count = len(unique_characters)

        if current_count > max_uniq_char_count:
            max_uniq_char_count = current_count
            max_uniq_char_word = word

    return max_uniq_char_word
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]