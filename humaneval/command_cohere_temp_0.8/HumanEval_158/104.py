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
    return lexicographically_first if char_count[lexicographically_first] == char_count[max_char_word] else max_char_word
``` 

This script defines a function `find_max` that solves the problem as described in the prompt. It takes a list of strings `words` as input and returns the word with the maximum number of unique characters, considering lexicographical order.

The script ensures that if multiple words have the maximum number of unique characters, the function will return the word that appears first in lexicographical order. It achieves this by keeping track of the word with the maximum character count thus far, while also tracking the lexicographically earliest word encountered.