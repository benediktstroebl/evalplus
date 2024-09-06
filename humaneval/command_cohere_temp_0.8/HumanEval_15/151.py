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
- The function `string_sequence(n)` uses the `map` function to convert the range of numbers from 0 to `n` into a list of strings and then uses `join` to concatenate them into a single string with spaces as separators.
- The tests check if the function behaves as expected for different values of `n`, ensuring that it produces the correct string representation of numbers up to `n`.