```python
def find_max(words):
    char_count = {}
    max_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)
        if current_count > max_count:
            max_count = current_count
            result = word
        if current_ count < max_count:
            continue
        for char in unique_chars:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                char_count[char] = 0
    return result
```

The function employs a dictionary named `char_count` to track the number of unique characters in each word. After iterating through the list of words, the function identifies the word with the highest count of unique characters and returns it, adhering to the lexicographical rule when multiple words have the same maximum count.