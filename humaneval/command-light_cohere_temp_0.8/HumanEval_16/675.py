```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isupper() and string})
```

Here, the code defines a function called `count_distinct_characters` which takes a string as input and returns the number of distinct characters in that string, regardless of case. This is done using a use of a generator expression and the `len()` function to calculate the length of the resulting list of distinct characters.