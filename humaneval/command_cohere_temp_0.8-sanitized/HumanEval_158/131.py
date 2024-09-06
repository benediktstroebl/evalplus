def find_max(words):
    char_count = {}
    max_count = 0
    result = None

    for word in words:
        unique_chars = set(word)
        count = len(unique_chars)

        if count > max_count:
            max_count = count
            result = word

    return result
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]