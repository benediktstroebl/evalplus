def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i, item in enumerate(lex):
        curr = set(item)
        if len(curr) == len(char_count):
            char_count[curr] = i
        else:
            char_count[curr] = i + 1
    return lex[char_count.get(set(lex[0]), len(lex))]