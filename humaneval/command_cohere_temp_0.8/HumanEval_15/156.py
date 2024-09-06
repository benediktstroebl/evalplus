```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code defines a function called `string_sequence`, which takes an integer argument `n`. Using the `range` function, it generates a sequence of numbers from 0 to `n` (inclusive). These numbers are then converted to strings using `map` and joined together with spaces using `join`. The resulting string is returned.

The tests assert that the function behaves as expected for two different inputs: `0` and `5`.