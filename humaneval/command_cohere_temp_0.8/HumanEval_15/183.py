```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script includes a function called `string_sequence` which takes an integer `n` as input and returns a string containing `n+1` space-separated numbers starting from 0 up to, and including, `n`. The function uses the `range` function to generate numbers from 0 to `n` and the `map` function to convert these numbers to strings. The `join` function is then used to concatenate these strings with spaces in between.

The tests check if the function behaves as expected for `n` values of 0 and 5, respectively. 

Would you like help with anything else?