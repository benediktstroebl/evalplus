```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This approach uses the `range()` and `map()` functions to generate numbers up to the input `n` and then converts them to strings using `str()`. The `join()` method is then used to concatenate the numbers into a single string separated by spaces. 

The example usage and test cases in the script demonstrate how the function works for different values of `n`. Adjusting the values of `n` in the test cells will validate various scenarios accordingly.