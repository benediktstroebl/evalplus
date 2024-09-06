```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This approach uses Python's `range` function to generate numbers up to `n`, and the `map` and `join` functions to turn this sequence of numbers into a string, with each number separated by a space.