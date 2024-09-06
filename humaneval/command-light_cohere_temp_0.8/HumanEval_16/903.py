```python
def count_distinct_characters(string):
    return len({c for c in string.md.lower() if c in string})
```

The function iterates through each character in the string and checks if it's in lowercase using the `lower()` method, then adds it to a set. If it's not, that means it's unique and not in the string, so it adds it to the set.

This is a self-contained solution, and does not require any additional variables or external functions to work.