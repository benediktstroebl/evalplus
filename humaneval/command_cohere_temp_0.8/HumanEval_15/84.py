```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet solves the problem using a generator expression in conjunction with the `join` method to concatenate the string representations of numbers from `0` up to and including `n` into a single string. The `range` function is used to generate the sequence of numbers.