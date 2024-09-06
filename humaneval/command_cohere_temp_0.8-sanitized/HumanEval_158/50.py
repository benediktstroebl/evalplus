def find_max(words):
    char_count = {}
    max_word = None
    max_word_index = None
    for index, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > (len(word) // 2) and (
            num_unique_chars == max(char_count.values()) or
            (num_unique_chars == char_count[word]) and
            word < max_word
        ):
            max_word = word
            max_word_index = index
        char_count[word] = num_unique_chars
    return max_word