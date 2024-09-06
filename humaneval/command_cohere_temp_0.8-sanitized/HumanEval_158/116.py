def find_max(words):
    max_unq = 0
    res = None
    for word in words:
        unq = set(word)
        if len(unq) > max_unq:
            max_unq = len(unq)
            res = word
    return res