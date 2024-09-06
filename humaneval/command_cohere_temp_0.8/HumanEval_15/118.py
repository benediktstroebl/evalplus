```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
``` 

This approach uses the `range()` and `map()` functions to generate numbers up to the input `n`, and `join()` to concatenate them into a single string with spaces.