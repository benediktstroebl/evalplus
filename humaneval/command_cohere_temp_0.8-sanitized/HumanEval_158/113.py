def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append((len(unique_chars), word))
    # Sorting lexicographical_order by the number of unique chars in descending order
    sorted_lexicographical_order = sorted(lexicographical_order, key=lambda x: x[0], reverse=True)
    return sorted_lexicographical_order[0][1]