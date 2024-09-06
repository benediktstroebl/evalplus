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
    
    return max_word

# Test cases
assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
```

This code defines a function `find_max` that solves the problem using a dictionary to count the number of unique characters in each word. The loop iterates through each word in the input list, calculates the count of unique characters, and compares it with the current maximum. After all words are processed, the function returns the word with the highest count of unique characters.