```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- The function `string_sequence(n)` utilizes Python's `range()` function to generate a list of numbers from 0 to `n` (inclusive).
- The `map(str, ...)` function is used to convert each item in the range to a string.
- The joined string is then returned with the `return ' '.join(map(str, range(n + 1)))`.
- The `test_string_sequence()` function verifies the behavior of `string_sequence()` against three different input values (`0`, `5`, and `10`).

This solution adheres to the problem statement and provides an accurate and efficient Python function for solving this problem.