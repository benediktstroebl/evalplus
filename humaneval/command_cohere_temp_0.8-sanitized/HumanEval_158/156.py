def find_max(words):
    max_set = max(set(word) for word in words)
    return max_set[:max_set.__len__()]