```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet uses the `range()` function to generate a list of numbers from 0 to `n` and then uses the `join()` method to concatenate these numbers into a single string with spaces as separators. The `str` function is used to convert the numbers in the range to strings.