```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

The function `string_sequence` uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `map` and `join` to convert these numbers into a space-delimited string. 

The test suite covers the cases for `0` and `5` as shown in the problem statement and the function passes both of them, ensuring its correctness.  This solution is efficient and easy to read, making it a good choice for this problem.