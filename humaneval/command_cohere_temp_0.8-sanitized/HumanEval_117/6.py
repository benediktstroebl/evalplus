def select_words(s, n):
    ls = []
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word = ""
    for c in s:
        if c == " ":
            if len(word) == 0:
                continue
            elif len(word) == 1:
                ls.append(word)
            else:
                word = ""
        elif c in consonants:
            word = word + c
        else:
            if len(word) == n:
                ls.append(word)
                word = ""
    if len(word) == n:
        ls.append(word)
    return ls