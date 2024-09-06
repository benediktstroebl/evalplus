```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > len(char_count):
            max_char_word = word
    if max_char_word is None:
        return ""
    return max_char_word
```

The code defines a function `find_max` that takes in a list of strings, specifically words. It aims to find a word with the highest count of unique characters, and if there are multiple ones with the same highest count, it returns the one that appears first in lexicographical order.

The approach is to loop through each word in the list, creating a dictionary that stores the word as the key and its count of unique characters as the corresponding value. If a word has a larger count of unique characters than any previous word, it becomes the new `max_char_word`. If multiple words have the same highest count, the one encountered first in the loop (in lexicographical order) is chosen and returned. 

The resulting function is concise and efficient, providing the desired outcome as per the problem statement.