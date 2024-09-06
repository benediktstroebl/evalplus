def find_max(words):
    char_count = {}
    max_word = None
    max_word_index = None
    
    for index, word in enumerate(words):
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        
        if max_word is None or char_count[word] > char_count[max_word]:
            max_word = word
            max_word_index = index
    
    if max_word is not None:
        return max_word
    else:
        return words[0]