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

The Python script defines a function `find_max` that solves the problem as described in the prompt. It iterates through the list of words, tracking the maximum number of unique characters seen so far. The function selects the first word in lexicographical order that achieves this maximum. The result is returned once the loop completes. This algorithm ensures that the desired output is produced for the given test cases.