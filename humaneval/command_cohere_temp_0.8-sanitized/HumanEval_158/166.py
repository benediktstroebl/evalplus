def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        char_count[num_unique_chars].append(word)
        if not max_word or (len(word) > len(max_word) and num_unique_chars == max_count):
            max_word = word
            max_count = num_unique_chars
    return max_word