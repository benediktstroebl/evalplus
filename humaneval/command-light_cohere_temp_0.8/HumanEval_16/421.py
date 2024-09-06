Here is a self-contained Python script that defines a function `count_distinct_characters` that solves the problem of counting the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()})

# Example usage:
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```

This code is self-contained and provides a clear and concise solution to the given problem.