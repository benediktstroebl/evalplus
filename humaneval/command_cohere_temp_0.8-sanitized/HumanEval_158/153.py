def find_max(words):
    char_count = {}
    max_word = None
    max_word_idx = None
    for idx, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word.count(char) for char in unique_chars}
            max_word = word
            max_word_idx = idx
        elif num_unique_chars == len(char_count) and word < max_word:
            max_word = word
            max_word_idx = idx
    return max_word