```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive.
    """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

The `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `map` and `join` to convert these numbers to a string and join them together with spaces as the delimiter. 

The `test_string_sequence` function verifies that the `string_sequence` function behaves as expected for different values of `n`. It checks if the output corresponds to the expected outputs based on the function docstring. 

To execute the test, simply call `test_string_sequence()` and the assert statements within will ensure the tests pass.