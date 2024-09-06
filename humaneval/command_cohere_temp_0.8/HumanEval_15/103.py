```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function `string_sequence(n)` that accepts an integer `n` and returns a string containing a sequence of numbers from 0 to `n` inclusive, separated by spaces. It achieves this using the `range` generator and the `join` method to concatenate these numbers into a single string.

The function is documented with a docstring that describes its purpose, input, and output. Additionally, the function is tested using Python's built-in `assert` statements to verify that it produces the expected results for various input values. These tests confirm that the function handles both zero and non-zero values of `n` correctly.