def find_max(words):
    words.sort()
    max_word = words[0]
    num_set = set()
    for word in words:
        num_set.update(word)
        if len(num_set) > len(max_word):
            max_word = word
    return max_word