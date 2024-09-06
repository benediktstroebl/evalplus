```python
def count_distinct_characters(string: str) -> int:
    return len(string.make_set())
```

This code defines a function that takes a string as input and uses the `make_set()` method from the set module to create a set of characters from the string. The `len()` function returns the unique characters, and the length of the resulting set is the number of distinct characters.