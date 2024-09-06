```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```
The function `string_sequence` takes an integer, n, as input and returns a string consisting of space-separated numbers ranging from 0 to n inclusive. This behavior is outlined in the function's docstring, which also provides example queries for testing. The test case specifically prints the return value of string_sequence(0), confirming that the function behaves as expected. In this case, it will print the string '0'.