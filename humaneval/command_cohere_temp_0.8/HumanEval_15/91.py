```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The function `string_sequence` takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` (inclusive) using the `range` and `map` functions. 

To showcase the function, the script also includes a test block that prints the result of calling `string_sequence` with an input of 0. The expected result is "0", as it's the only number that satisfies the problem's conditions.