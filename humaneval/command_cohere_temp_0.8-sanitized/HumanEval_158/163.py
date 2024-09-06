def find_max(words):
    words.sort()
    max_set = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set):
            max_set = char_set
    return words[max_set == max_set][0]