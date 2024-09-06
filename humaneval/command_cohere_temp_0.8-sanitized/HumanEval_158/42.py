def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > max_char_count:
            max_char_count = char_count[word]
            max_word = word
            
    return max_word
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]