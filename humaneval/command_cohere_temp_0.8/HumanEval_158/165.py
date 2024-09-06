```python
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
```

The function employs a dictionary (`char_count`) to keep track of candidates words with a specific number of unique characters. After iterating through the input list of words, the function selects the word with the most unique characters. If multiple words have the most unique characters, the lexicographically earliest word is selected. 

This approach ensures due consideration of word length and uniqueness of characters.