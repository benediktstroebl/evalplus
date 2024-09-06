def find_max(words):
    words.sort()
    max_char = 0
    result = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_char:
            max_char = len(unique_chars)
            result = word
    return result