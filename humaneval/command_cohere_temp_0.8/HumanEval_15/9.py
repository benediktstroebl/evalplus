```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
derive_answers = [('0', 0), ('5', 5)]
for expected, n in derive_answers:
    assert string_sequence(n) == expected
```

The `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `map` and `join` to convert these numbers into a space-delimited string. The tests validate that the function behaves as expected for different values of `n`.