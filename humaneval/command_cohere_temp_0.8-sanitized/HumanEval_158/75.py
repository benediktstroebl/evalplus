def find_max(words):
    max_num_chars = 0
    max_word = None

    for word in words:
        num_chars = len(set(word))
        if num_chars > max_num_chars:
            max_num_chars = num_Chars
            max_word = word

    return max_word
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]