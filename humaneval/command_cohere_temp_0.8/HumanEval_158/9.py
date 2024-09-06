```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_characters = set(word)
        char_count[word] = len(unique_characters)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_char_word = max(char_count, key=char_count.get)
    return max_char_char_word if lexicographically_first == max_char_word else lexicographically_first
```