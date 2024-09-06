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

The Python script defines a function `find_max` that solves the problem statement. It iterates through the list of words, using a dictionary to keep track of the unique characters in each word. It then identifies the word with the highest count of unique characters, or the word with the highest count that alphabetically precedes any other equally populous word. 

Here's an example usage of the function under a variety of test cases:
```python
# Example test cases
print(find_max(["name", "of", "string"]))      # Output: "string"
print(find_max(["name", "enam", "game"]))     # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))     # Output: "aaaaaaa"
```

This functional approach ensures that the answer is correct and adaptable to diverse scenarios.