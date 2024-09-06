def find_max(words):
    char_count = {}
    max_count = 0
    result = None

    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)

        if current_count > max_count:
            max_count = current_count
            result = word

    return result
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]