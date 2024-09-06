```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function called `string_sequence` which takes an integer value `n` as input and returns a string consisting of space-separated numbers starting from 0 up to and including `n`. The function achieves this by using the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses the `map` function to convert each number to a string, and the `join` method to concatenate these strings with spaces in between.

The comments above the function describe its purpose and its behavior given different input values. The final part of the script includes a couple of test cases that print the return values of the function for `n = 0` and `n = 5` to validate its correctness. 

The code block adheres to the problem request and provides a self-contained Python script with a function that solves the specified task. It also includes tests to ensure the function's correctness. 

You can run this code to see the function's behavior for different input values.