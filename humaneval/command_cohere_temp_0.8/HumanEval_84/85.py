Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as input and converts it to a string `s`. It then joins this string together to form a binary string, which is then converted back to an integer using `int()`. The `format()` method is used to convert this integer back to a binary string for the final output.

The previous response's code snippet can be pasted into a Python file and run independently to execute the function and verify its correctness. You can test it with various input values to confirm that it satisfies the specified constraints and conditions.