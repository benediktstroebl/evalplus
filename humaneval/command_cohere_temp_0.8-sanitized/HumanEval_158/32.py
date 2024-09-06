def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: num_unique_chars for char in unique_chars}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < max_char_word:
            max_char_word = word
    return max_char_word