```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This code defines a function called `count_distinct_characters`, which takes a string as input and returns the number of distinct characters in the string, regardless of case. The function achieves this by using the set and `lower()` methods to remove duplicate characters and ensure uniqueness. The function passes all tests as well and is self-contained, meaning it does not require any external variables or functions to work.