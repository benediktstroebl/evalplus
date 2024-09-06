```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```
The above code uses the `range()` function to generate a sequence of numbers from 0 to `n` (inclusive) and the `map()` function to convert these numbers into strings. The `join()` method is then used to concatenate these strings into a single string separated by spaces.