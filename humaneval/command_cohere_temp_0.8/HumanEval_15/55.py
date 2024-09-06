```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the function uses the `range()` and `map()` functions to generate numbers up to `n` and then converts them to strings using `str()`. The `join()` function is then used to concatenate the strings together into a single string with spaces in between. 

To follow the specified docstring, the function returns a string starting from 0 up to including `n` parametric value. Thus, using this function with different input values returns the following results:
```
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```