def find_max(words):
    max_uniq_char_word = None
    max_uniq_char_count = 0
    
    for word in words:
        uniq_char_count = len(set(word))
        if uniq_char_count > max_uniq_char_count:
            max_uniq_char_word = word
            max_uniq_char_count = uniq_char_count
        
    return max_uniq_char_word