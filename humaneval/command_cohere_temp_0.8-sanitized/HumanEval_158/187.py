def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: num_unique_chars for char, num_chars in zip(word, enumerate(unique_chars))}
        elif num_unique_chars == len(char_count):
            for char, num_chars in zip(word, enumerate(unique_chars)):
                if char in char_count and num_chars > char_count[char]:
                    char_count[char] = num_chars
        if max_char_word is None or (len(char_count) == 1 and word < max_char_word):
            max_char_word = word
    return max_char_word