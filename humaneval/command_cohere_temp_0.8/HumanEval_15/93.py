```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

The `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `map` and `join` to convert these numbers to a string with space-separated format.

The `test_string_sequence` function verifies the behavior of the `string_sequence` function for multiple input scenarios and asserts the expected output. 

Running the test function helps confirm that the `string_sequence` function works as expected. This approach helps ensure the function behaves similarly with different inputs.  You can always add more tests to cover other scenarios or edge cases if necessary.  Feel free to adapt this block according to your specific needs or to explore other problem-solving strategies.