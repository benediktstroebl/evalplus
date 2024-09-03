def find_max(words):
    words.sort(max_count=lambda w: len(set(c for c in w)))
    return words[max_count]