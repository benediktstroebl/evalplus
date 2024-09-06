def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i in range(len(lex)):
        curr = set(lex[i])
        total_char = len(curr)
        unique_count = len(curr) - 1
        if unique_count not in char_count:
            char_count[unique_count] = []
        char_count[unique_count].append((total_char, lex[i]))
    max_index = max(char_count, key=lambda x: len(x[0]))[0]
    return lex[max_index][0]