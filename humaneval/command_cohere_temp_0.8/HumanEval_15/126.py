```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- The function `string_sequence(n)` utilizes Python's `range()` generator and the `map()` function to convert each integer to a string, delimited by spaces.
- The `test_string_sequence()` function verifies that the `string_sequence()` function behaves as expected for different values of `n`.
- The final call to `test_string_sequence()` ensures that the function behaves correctly.