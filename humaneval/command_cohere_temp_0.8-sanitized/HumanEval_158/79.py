def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_char_word = min(char_count, key=char_count.get)
    return lexicographically_first if char_count[lexicographically_first] == char_count[max_char_word] else max_char_word