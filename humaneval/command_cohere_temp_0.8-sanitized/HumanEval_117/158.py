def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = []
    word = ""
    for c in s:
        if c.isalpha():
            if c in consonants:
                word += c
            else:
                if len(word) == n:
                    words.append(word)
                word = ""
    if len(word) == n:
        words.append(word)
    return words if len(s) != 0 else []