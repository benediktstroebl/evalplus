```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string. string if char == substring)
```

This code defines a function called `how_many_times` that returns the number of times a given substring can be found in the original string. The function uses a `sum()` function along with a list comprehension to count the number of occurrences of the substring.