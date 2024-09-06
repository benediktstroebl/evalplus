def find_max(words):
    max_unq = 0
    res = None
    for w in words:
        unq = set(w)
        if len(unq) > max_unq:
            max_unq = len(unq)
            res = w
    return res