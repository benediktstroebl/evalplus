def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in zip(unique_chars, word)}
        elif len(unique_chars) == len(char_count):
            for char in unique_chars:
                if char not in char_count:
                    char_count = {char: word for word, char in zip(unique_chars, word)}
                    break
            else:
                if word < max_word or max_word is None:
                    max_word = word
    return max_word