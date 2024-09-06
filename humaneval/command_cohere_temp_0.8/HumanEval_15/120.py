```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This approach uses the `range()` and `map()` functions to generate a list of numbers from `0` to `n` inclusive, and then joins these numbers into a single string with spaces using the `join()` method. The `str` function is used to convert the `range` objects to strings.