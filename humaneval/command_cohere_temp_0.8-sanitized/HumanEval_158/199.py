def find_max(words):
    char_count = {}
    lexic_front = []
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] == max(char_count.values()):
            lexic_front.append(word)
            
    return lexic_front[0] if lexic_front else None