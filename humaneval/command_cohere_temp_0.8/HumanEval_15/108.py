```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))   # Expected output: 0
print(string_sequence(5))    # Expected output: 0 1 2 3 4 5
```

This script defines a function called `string_sequence`, which takes an integer n as input and returns a string consisting of space-delimited numbers ranging from 0 to n inclusive. The `map` function is used to convert the range of numbers into a list of string values, and the `join` method concatenates these strings into a single string with spaces in between.

The script also includes simple test cases that print the output of `string_sequence` for values 0 and 5, and the expected output is also provided. The function and tests are fully self-contained in this code block, as required by the prompt.