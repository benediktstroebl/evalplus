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

To ensure the function is correct, two tests are added: one for the base case of zero, and another for a higher number. The `test_string_sequence()` function verifies the output of `string_sequence()` against the expected results. You can use these tests to ensure that the function behaves as expected. 

To execute the tests, you would run `test_string_sequence()` after running the `string_sequence` function definition.