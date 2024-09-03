def find_max(words):
    return words[0] if len(set(words[0])) > len(set(words)) else words[1]