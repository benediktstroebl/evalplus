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

To ensure our function stays flexible and robust, we've added a test suite. The `test_string_sequence()` function verifies the output of `string_sequence()` against expected results for different input values. This way, if anything changes within the function's behavior, the tests will alert us, ensuring it consistently produces correct results.