```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet includes a function called `string_sequence` that takes an integer argument `n`. It employs the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses the `join` method to convert this sequence into a single string, separated by spaces. The function is encapsulated with tests to validate its behavior against specific inputs.