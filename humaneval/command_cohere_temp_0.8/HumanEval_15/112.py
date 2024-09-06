```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```
The function `string_sequence` takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` (inclusive) using the `range` and `str` modules and the `map` and `join` functions.  The test case prints out the result for `n` equal to 0, which should be the string '0'. 
```bash
0
```