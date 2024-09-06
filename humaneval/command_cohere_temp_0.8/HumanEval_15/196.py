```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-separated numbers ranging from 0 to `n` (inclusive) using the `range` and `str` mapping functions. The function is tested twice with the tests exposed in the markdown docstring to ensure it conforms to the expected behavior.