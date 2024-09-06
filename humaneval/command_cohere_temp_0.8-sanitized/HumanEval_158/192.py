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
    
    for char_count_key, word_entries in char_count.items():
        sorted_word_entries = sorted(word_entries)
        if max_word is None or max_word_index == sorted_word_entries[0][1]:
            max_word = sorted_word_entries[0][0]
            max_word_index = sorted_word_entries[0][1]
        elif max_word_index > sorted_word_entries[0][1]:
            max_word = sorted_word_entries[0][0]
            max_word_index = sorted_word_entries[0][1]
    
    return max_word