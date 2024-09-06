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
    
    for num_chars, candidates in char_count.items():
        if len(candidates) == 1 or (len(candidates) > 1 and max_word_index is None):
            max_word, max_word_index = max(candidates, key=lambda x: x[1])
    
    return max_word