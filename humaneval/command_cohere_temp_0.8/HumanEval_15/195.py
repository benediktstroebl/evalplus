```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- The function `string_sequence(n)` uses the `range()` and `map()` functions to generate numbers from 0 to `n` (inclusive) and converts them to strings.
- The `map()` function transforms each number into a string, and `join()` converts the list of strings into one string, separated by spaces.
- The `test_string_sequence()` function verifies that the `string_sequence()` function behaves as expected for different values of `n`.
- The final line, `test_string_sequence()`, runs the tests to ensure that the function `string_sequence()` correctly solves the problem.