def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i in range(len(lex)):
        curr = set(lex[i])
        total_char = len(curr)
        count = len(char_count)
        for c in curr:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        for c in char_count:
            char_count[c] += (total_char - char_count[c]) * count
        if len(char_count) == 1:
            return lex[i]
    return lex[0]