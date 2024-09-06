def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append([word, len(unique_chars)])
    max_unique_chars = max(char_count.values())
    max_entry = max(lexicographical_order, key=lambda x: x[1])
    return max_entry[0] if max_entry[1] == max_unique_chars else words[lexicographical_order.index(max_entry)]