```python
def find_max(words):
    words.sort()
    max_char_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        char_count = len(unique_chars)
        if char_count > max_char_count:
            max_char_count = char_count
            result = word
    return result
```

The function sorts the list of words lexicographically and then iterates through the words, counting the number of unique characters in each word and comparing this count to the maximum count seen so far. The word with the highest number of unique characters that meets the criteria is returned as the result, and if multiple words have the same maximum unique character count, the first one in lexicographical order is chosen as per the specified criteria. 

This approach is efficient because it only needs to traverse the list of words once, and it can find the maximum unique character count efficiently within a single pass.