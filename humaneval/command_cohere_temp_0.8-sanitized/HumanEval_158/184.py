def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        char_count[num_unique_chars].append((word, len(word)))
        if max_word is None or num_unique_chars > len(set(max_word)):
            max_word = word
    return max_word