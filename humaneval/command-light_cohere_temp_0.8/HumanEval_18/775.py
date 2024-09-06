```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string. string(substring))
```

This function uses a generator expression to iterate over every character in the input string, and for each character it checks if it's a match for the corresponding substring. The function returns the
the total number of matches found.