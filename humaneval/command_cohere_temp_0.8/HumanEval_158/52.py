```python
def find_max(words):
    words.sort()
    max_char = 0
    result = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_char:
            max_char = len(unique_chars)
            result = word
    return result
```

The function `find_max` accepts a list of strings, sorts the list, and then iterates over each word. It uses a set data structure to calculate the unique characters in each word and compares this quantity with the maximum count seen so far ('max_char'). The word that yields the maximum number of unique characters, or the first one in lexicographical order among such words, is chosen as the final result. 

This approach ensures the efficiency of the function and makes it capable of handling various scenarios correctly.