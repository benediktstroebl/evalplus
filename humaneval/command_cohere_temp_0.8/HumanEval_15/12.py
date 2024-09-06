```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))   # Expected output: 0
print(string_sequence(5))    # Expected output: 0 1 2 3 4 5
``` 

The above code snippet uses the `range()` function to generate a list of numbers from `0` up to `n` and then uses `str` conversion and `join()` method to concatenate these numbers into a single string where these numbers are separated by spaces. It also includes a docstring to explain its behavior and clarify the function's purpose.