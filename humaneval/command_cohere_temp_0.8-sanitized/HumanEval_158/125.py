def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for w in words:
        uniq = len(set(w))
        if uniq > max_uniq:
            max_uniq = uniq
            result = w
    return result