def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i in range(len(lex)):
        temp = set(lex[i])
        char_count[lex[i]] = len(temp)
    return char_count[lex[0]]