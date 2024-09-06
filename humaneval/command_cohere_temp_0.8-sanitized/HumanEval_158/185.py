def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_characters = set(word)
        char_count[word] = len(unique_characters)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_count = max(char_count.values())
    return char_count[lexicographically_first] if char_count[lexicographically_first] == max_count else lexicographically_first