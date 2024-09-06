def find_max(words):
    char_count = {}
    max_word = None
    max_word_idx = None
    for idx, word in enumerate(words):
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_word is None or char_count[word] > char_count[max_word]:
            max_word = word
            max_word_idx = idx
    return words[max_word_idx]