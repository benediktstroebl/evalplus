```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```

The above problem can be solved using the built-in `range()` and `map()` functions in conjunction with the `join()` method. The `range()` function produces a series of numbers starting from 0 up to `n` (inclusive) whereas the `map()` function transforms each item in that sequence into a string counterpart. Finally, the `join()` method combines all the string outputs from the `map()` function together into one single string, separated by spaces.