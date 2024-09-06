```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters() if c not keyboard.isalnum(c)})
```

The function uses the built-in `islower()` method to convert all characters to lowercase and then uses the `len()` function to get the length of the resulting set of characters.