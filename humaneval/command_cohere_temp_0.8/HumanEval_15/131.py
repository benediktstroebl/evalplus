```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```

The `string_sequence` function uses the `range()` and `map()` functions to generate numbers from 0 to `n`, inclusive, and then joins these numbers into a single string with spaces as the delimiter. The tests verify that the function behaves as expected for different input values of `n`, ensuring the output is a string containing the sequence of numbers from 0 to `n` (inclusive) with proper spacing.  Such that, `string_sequence(0)` returns '0', and `string_sequence(5)` returns '0 1 2 3 4 5'.