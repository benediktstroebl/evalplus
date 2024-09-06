def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        uniq = set(word)
        if len(uniq) > max_uniq:
            max_uniq = len(uniq)
            max_word = word
    return max_word