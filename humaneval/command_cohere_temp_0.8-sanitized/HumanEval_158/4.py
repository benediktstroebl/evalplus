def find_max(words):
    char_count = {}
    max_word = None
    max_word_idx = None
    
    for idx, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        
        char_count[num_unique_chars].append((word, idx))
    
    for num_chars, word_idx_list in char_count.items():
        # Sort words based on lexicographical order and select the first one
        word_idx_list.sort(key=lambda x: x[0])
        if max_word is None or word_idx_list[0][0] > max_word:
            max_word = word_idx_list[0][0]
            max_word_idx = word_idx_list[0][1]
    
    return max_word