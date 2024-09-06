def find_max(words):
    char_count = {}
    lexicographical_max = None

    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)

        if char_count[word] > len(char_count):
            lexicographical_max = word

    return lexicographical_max