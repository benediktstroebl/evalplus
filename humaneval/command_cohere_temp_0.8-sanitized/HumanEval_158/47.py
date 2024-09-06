def find_max(words):
    char_count = {}
    max_count = 0
    lexicographically_earliest = None

    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)
        if current_count > max_count:
            max_count = current_count
            lexicographically_earliest = word

    return lexicographically_earliest