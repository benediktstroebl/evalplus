```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The function `string_sequence` accepts an integer n and returns a string consisting of space-separated numbers ranging from 0 to n inclusive. It achieves this by using the range function to generate a sequence of numbers starting from 0 up to `n` (inclusive), and then uses the `join` method to concatenate these numbers into a single string with spaces as separators. 

The test suite provides an example of how the function performs for a specific input, printing the result to the console.