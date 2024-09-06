```python
def find_max(words):
    max_unq = 0
    res = ""
    for w in words:
        unq = set(w)
        if len(unq) > max_unq:
            max_unq = len(unq)
            res = w
    return res
```

This Python script defines a function `find_max` that solves the problem as described in the prompt. It iterates through the list of words, calculates the unique characters in each word, and keeps track of the maximum count seen so far. The lexicographically earliest word with the maximum count is returned as the result. The `set()` function is used to remove duplicate characters from a string, and the loop iterates through the words, comparing the unique characters encountered against the maximum seen so far.

This approach has a time complexity of `O(n)` since it requires iterating through the list of words once to find the word with the maximum count of unique characters.