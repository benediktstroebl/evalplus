```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet includes a function called `string_sequence` which takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` inclusive. The function achieves this by using the `range` function to generate a sequence of numbers from 0 to `n` and then applying the `map` function to convert each number to a string. The `join` function is applied to concatenate the strings with spaces in between.

The code then includes some tests that check the behavior of the `string_sequence` function for various input values. The `assert` statements verify that the function produces the expected output for the given inputs.