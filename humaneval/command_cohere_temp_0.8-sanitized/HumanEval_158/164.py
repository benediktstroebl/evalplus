def find_max(words):
    max_uniq = 0
    mx = None
    for w in words:
        uniq = set(w)
        if len(uniq) > max_uniq:
            max_uniq = len(uniq)
            mx = w
    return mx