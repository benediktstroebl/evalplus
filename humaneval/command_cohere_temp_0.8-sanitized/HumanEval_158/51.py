def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)
        
        if current_count > max_char_count:
            max_char_count = current_count
            max_word = word
            
    return max_word