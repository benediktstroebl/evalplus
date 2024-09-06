```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
``` 

This code snippet uses the `range()` and `map()` functions to generate numbers up to the input value `n` and convert them to strings, respectively. The `join()` function is then used to concatenate these strings into a single string with spaces in between. 

The problem assertion tests are included to validate the function behavior. Editing the `n` value in the assert functions lets you conveniently test different scenarios.