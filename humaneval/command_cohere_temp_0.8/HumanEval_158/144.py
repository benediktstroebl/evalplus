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

The function `find_max` sorts the list of words lexicographically and then iterates through the list. For each word, it calculates the number of unique characters using a set and compares this count to the maximum count seen so far. If the current word has more unique characters, it updates the result and the maximum count. Ultimately, the function returns the word with the maximum number of unique characters.