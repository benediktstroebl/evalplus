def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > len(char_count):
            max_char_word = word
    if max_char_word is None:
        return ""
    return max_char_word