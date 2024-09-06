```python
def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        current_char_count = len(unique_chars)
        
        if current_char_count > max_char_count:
            max_char_count = current_char_count
            max_word = word
        elif current_char_count == max_char_count:
            if word < max_word:
                max_word = word
    
    return max_word
```

The Python script defines a function `find_max` that solves the problem statement. It iterates through the list of words, tracking the number of unique characters in each word using a dictionary `char_count`. When a word contains a number of unique characters greater than the previously recorded maximum, it updates `max_char_count` and stores the corresponding word in `max_word`. If the word has the same number of unique characters as the current maximum, it checks the lexicographical order and updates `max_word` if the current word is greater. At the end of the loop, it returns the maximum word.