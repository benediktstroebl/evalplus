```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```

The above `string_sequence` function uses the `range()` and `map()` functions to generate a list of numbers from 0 to `n` and then uses `join()` to concatenate these numbers into a single string separated by spaces. 

The tests verify that the function works for different values of `n`, ensuring that the resulting string contains the expected sequence of numbers.