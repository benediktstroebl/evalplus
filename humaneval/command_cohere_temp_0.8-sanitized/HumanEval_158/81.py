def find_max(words):
    words.sort()
    max_set = set()
    max_word = ""
    for word in words:
        curr_set = set(word)
        if len(curr_set) > len(max_set):
            max_set = curr_set
            max_word = word
    return max_word