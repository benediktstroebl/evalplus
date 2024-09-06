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
- This Python script defines a function `string_sequence(n)` that accepts an integer `n` and returns a string containing space-separated integers ranging from 0 to `n` (inclusive) using the `range` generator and the `str` constructor to convert these numbers into strings, and finally joins these strings together using spaces as a separator with the `join` method of the `str` constructor.
- The script also includes a test function `test_string_sequence` defined using the Python `pytest` framework. This function tests the `string_sequence` function with three different input values (0, 5, 10) and asserts that the output from the function corresponds to the expected output.
- The final line of the script executes the test function to validate the `string_sequence` function. 

This code demonstrates Python's str expression, map, and range generators, as well exploitation of the `pytest` testing framework to ensure the correct functionality of the `string_sequence` function. 

Please feel free to ask any questions or to further clarify the reasoning behind this code.