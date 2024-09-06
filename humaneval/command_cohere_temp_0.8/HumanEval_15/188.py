```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```
The above code uses the `range()` function to generate a sequence of numbers up to the specified number (`n`) and then uses `str()` and `map()` functions to convert these numbers into a string with integers separated by spaces.