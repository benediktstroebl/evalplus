```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: num_unique_chars for char in unique_chars}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < max_char_word:
            max_char_word = word
    return max_char_word
```

The `find_max` function takes a list of words as input and calculates the number of unique characters in each word using a dictionary. It iterates through the list and keeps track of the word with the highest count of unique characters. If there are multiple words with the same count, it selects the one that appears first in lexicographical order. The function output matches the given test cases.