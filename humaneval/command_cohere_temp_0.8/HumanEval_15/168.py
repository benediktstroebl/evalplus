```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The above code uses the `range()` function to generate a list of numbers from 0 to `n` and then uses `map()` and `str` to convert these numbers into strings and joins them with spaces using the `join()` method. The `print()` function is used to print the result for `n = 0` to verify the output. The output of the above code is as follows:
```
0
```