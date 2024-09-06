```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

The `string_sequence` function uses the `range` and `map` functions to generate a list of numbers from 0 to `n` (inclusive) and then joins these numbers into a single string with spaces as the delimiter. The `test_string_sequence` function verifies that the output of `string_sequence` is correct for three different input values (`0`, `5`, and `10`). The final line calls this test function to validate the behavior of the `string_sequence` function.