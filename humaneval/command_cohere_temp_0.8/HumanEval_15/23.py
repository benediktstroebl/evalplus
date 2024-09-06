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
- The function `string_sequence(n)` utilizes Python's `range()` function to generate a sequence of numbers from 0 to `n` (inclusive).
- The `map()` function is then used to convert these numbers to strings.
- Finally, the `join()` method is applied to concatenate the separated string values into a single string, separated by spaces.

The provided test cases verify that the function behaves as expected for different values of `n`, ensuring correct conversion of numbers to strings and proper spacing.