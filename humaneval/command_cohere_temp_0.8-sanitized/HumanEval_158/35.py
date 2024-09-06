def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique_chars = len(set(word))
        if unique_chars not in char_count:
            char_count[unique_chars] = []
        char_count[unique_chars].append(word)
        lexic_front[unique_chars] = word

    return min(lexic_front, key=lexic_front.get)