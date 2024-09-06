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

### Explanation:
- This Python code defines the `string_sequence` function that accepts a single integer argument `n`.
- It uses the `range` function to generate a list of numbers from 0 to `n` (inclusive) due to the `+ 1` in the range function.
- The `map` function is then used to convert these numbers to strings, and the `join` method joins these strings together with spaces.
- The `test_string_sequence` function provides test cases to validate the behavior of `string_sequence`. It uses the `assert` statement to ensure the expected output matches the output of the function with the given inputs.
- The final call to `test_string_sequence` ensures that the function behaves as expected. 
These tests will fail if the code or function does not handle the specified test cases correctly.