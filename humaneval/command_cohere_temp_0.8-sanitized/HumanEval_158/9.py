def find_max(words):
    char_count = {}
    max_word = None
    max_word_index = None
    
    for index, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        
        char_count[num_unique_chars].append((word, index))
    
    for char_count_key, word_list in char_count.items():
        if max_word is None or len(word_list) > len(max_word_list):
            max_word_list = word_list
            max_word_index = char_count_key
            max_word = sorted(word_list)[0][0]
    
    return max_word