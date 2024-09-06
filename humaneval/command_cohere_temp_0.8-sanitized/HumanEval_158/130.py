def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique_chars = len(set(word))
        if unique_chars not in char_count:
            char_count[unique_Chars] = 1
        else:
            char_count[unique_chars] += 1
        lexic_front[unique_chars] = word

    max_count = max(char_count.values())
    return min(lexic_front, key=lambda x: char_count[x] != max_count)