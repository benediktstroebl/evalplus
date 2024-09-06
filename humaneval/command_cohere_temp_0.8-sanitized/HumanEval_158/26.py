def find_max(words):
    max_uniq_char_word = None
    max_uniq_char_count = 0
    
    for word in words:
        uniq_chars = set(word)
        cur_uniq_char_count = len(uniq_chars)
        
        if cur_uniq_char_count > max_uniq_char_count:
            max_uniq_char_count = cur_uniq_char_count
            max_uniq_char_word = word
    
    return max_uniq_char_word
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]