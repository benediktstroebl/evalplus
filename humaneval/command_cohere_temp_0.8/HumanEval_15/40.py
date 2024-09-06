```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
``` 

This code snippet uses the `range()` function to generate a sequence of numbers from 0 to `n`, and the `map()` function to convert these numbers into a string array. The `join()` method is then applied to concatenate the array of strings into a single string, and finally, the function returns the resulting string.