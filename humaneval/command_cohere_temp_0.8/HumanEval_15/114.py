```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The function `string_sequence` takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` (inclusive) using the `range` and `str` modules and the `map` and `join` functions. 

The test code is removed as it is not a direct part of the function, and the specification of the problem is enough to understand its behavior.