```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script includes a function called `string_sequence` which takes an integer `n` as input and returns a string containing space-separated numbers starting from 0 up to (and including) `n`. The function uses the `range` function to generate numbers from 0 to `n` and the `map` function to convert these numbers to strings, and finally, the `join` function concatenates these strings with spaces in between.

The comments also include test cases to verify the correctness of the function. It checks for the base case when `n` is 0, and also when `n` is 5, confirming that the function produces the correct output for both cases.

To run this code, you can copy and paste it into a Python interpreter or save it in a file with a .py extension such as `string_sequence.py`. You can then execute it by typing `python string_sequence.py` in the command line.