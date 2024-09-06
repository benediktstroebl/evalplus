```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This approach uses the `range()` and `map()` functions to generate numbers up to the input `n`, and `str()` to convert these generated numbers into strings, and finally, the `join()` method to concatenate these strings with spaces in between.