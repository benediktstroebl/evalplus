```python
def find_max(words):
    """Return the word with the maximum number of unique characters.
    If multiple strings have the maximum number of unique characters,
    return the lexicographically smallest one.
    """
    max_len = 0
    result = ""
    for word in words:
        if len(set(word)) > max_len:
            max_len = len(set(word))
            result = word
        elif len(set(word)) == max_len and word < result:
            result = word
    return result
```