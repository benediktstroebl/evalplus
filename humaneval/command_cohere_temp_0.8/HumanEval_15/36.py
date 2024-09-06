```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the built-in `range()` and `map()` functions in Python. The `range()` function creates a sequence of numbers starting from 0 up to the specified number (`n`) inclusively. The `map()` function then applies the `str` function to each element in this sequence, converting it to a string representation. Finally, the `join()` method is used to concatenate these string representations into a single string, separated by spaces.

The `string_sequence()` function encapsulates this process, allowing us to generate the desired string sequence based on the input `n`. For example, if `n` is 5, the function will return "0 1 2 3 4 5".