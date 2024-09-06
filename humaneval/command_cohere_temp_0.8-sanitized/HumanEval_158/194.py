def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in unique_chars.items()}
        if max_word is None or len(char_count) < len(max_word):
            max_word = word
    return max_word