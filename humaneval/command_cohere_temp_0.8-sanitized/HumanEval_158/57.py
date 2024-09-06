def find_max(words):
    words.sort()
    max_char_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        char_count = len(unique_chars)
        if char_count > max_char_count:
            max_char_count = char_count
            result = word
    return result