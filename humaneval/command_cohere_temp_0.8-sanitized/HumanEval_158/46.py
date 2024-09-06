def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append((char_count[word], word))
    return min(lexicographical_order)[1]