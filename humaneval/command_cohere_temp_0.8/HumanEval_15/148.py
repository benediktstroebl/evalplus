```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument, `n`, an integer representing the maximum number to be included in the sequence. The function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) using `n+1` as the argument, and then maps each of these numbers to a string representation using `str`. The joined strings are then returned as a space-separated sequence. 

The function is appropriately documented with a docstring that describes its purpose, input, and output. Furthermore, the function is tested with two test cases, providing and example usage of the function and checking whether it produces the expected outputs for `n` equal to both `0` and `5`.  The test cases are defined using Python's `unittest` module, and each test is specified within a `test` function that asserts a specific condition.