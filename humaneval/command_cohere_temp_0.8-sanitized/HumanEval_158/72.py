def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word for char, word in zip(unique_chars, [word])}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < char_count.values()[0]:
            max_char_word = word
    return max_char_word