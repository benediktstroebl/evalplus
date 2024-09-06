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
    
    for num_chars, candidates in char_count.items():
        if max_word is None or len(max_word) < len(candidates[0][0]):
            max_word = candidates[0][0]
            max_word_idx = candidates[0][1]
        elif len(max_word) == len(candidates[0][0]):
            for word, idx in candidates:
                if max_word < word:
                    max_word = word
                    max_word_idx = idx
    
    return max_word