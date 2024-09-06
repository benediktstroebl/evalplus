```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single integer argument `n`. This function utilizes the `range` function to generate a sequence of numbers from 0 to `n`, inclusive, and then employs the `map` function to convert these numbers to strings. Lastly, the `join` function is used to concatenate these strings into one string, separated by spaces, and this final string is returned.

Here is a test case to ensure the function is working correctly:
```python
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
```

The above `test_string_sequence` function calls `string_sequence` with three different arguments (0, 5, 10), and verifies that the returned values are correct. Thus, the `test_string_sequence` function ensures that `string_sequence` function is functioning properly.  This test case can be added to the script alongside the function to validate the correctness of the function.