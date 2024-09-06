def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        char_count[num_unique_chars].append(word)
        if max_char_word is None or (
            num_unique_chars > len(set(max_char_word))
            and word < max_char_word
        ):
            max_char_word = word
    return max_char_word