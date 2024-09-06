def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique = set(word)
        count = len(unique)
        if count not in char_count:
            char_count[count] = []
        char_count[count].append(word)
        lexic_front[word] = count
    # Check if there's a lexicographically earlier candidate for each count.
    for word in words:
        count = lexic_front.get(word)
        if count:
            if len(char_count[count]) > 1:
                del lexic_front[char_count[count][1]]
            char_count[count].remove(char_count[count][0])
            char_count[count][0] = word
    max_count = max(list(char_count.keys()), key=lambda x: char_count[x])
    return char_count[max_count][0]