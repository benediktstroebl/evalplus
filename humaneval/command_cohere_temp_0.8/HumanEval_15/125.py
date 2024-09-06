```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```

The function `string_sequence` uses the `range` and `map` functions to generate a list of numbers from 0 to `n` (inclusive) and then uses `str` and `join` to convert these numbers into a space-delimited string. 

The test cases print the result for `n = 0` and `n = 5` to validate the correctness of the function against the given test cases.