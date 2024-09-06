def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for word in words:
        uniq = len(set(word))
        if uniq > max_uniq:
            max_uniq = uniq
            result = word
    return result