```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_count = max(char_count.values())
    return char_count[lexicographically_first] if char_count[lexicographically_first] == max_count else lexicographically_first
```

The code defines a function `find_max` that takes in a list of words, it first counts the number of unique characters in each word and stores them in a dictionary `char_count`. It then identifies the word with the highest count of unique characters among the words, if there are multiple words with the same highest count, it returns the one that appears first in lexicographical order. The code leverages Python's `set` to efficiently calculate unique characters, and the `lexicographically_first` variable ensures we always have the first occurrence of the maximum unique character count for returning if there's a tie.