def find_max(words):
    max_num_uniq_chars = 0
    max_word = None

    for word in words:
        num_uniq_chars = len(set(word))
        if num_uniq_chars > max_num_uniq_chars:
            max_num_uniq_chars = num_uniq_chars
            max_word = word

    return max_word
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]