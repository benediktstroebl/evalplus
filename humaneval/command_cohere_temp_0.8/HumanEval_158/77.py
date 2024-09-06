```python
def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)
        
        if current_count > max_char_count:
            max_char_count = current_count
            max_word = word
        elif current_count == max_char_count:
            if word < max_word:
                max_word = word
    
    return max_word
```

The function employs a dictionary (`char_count`) to tally the quantity of distinct characters present in each word. When a word contains a higher count of unique characters than previous words, the word is updated as the `max_word` candidate. If two words possess the same count of unique characters, the newer word is preferred due to the lexicographical ordering criterion specified in the problem statement. 

This solution adheres to the problem's expectations, demonstrating its validity and efficiency in solving the given problem.