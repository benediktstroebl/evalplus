```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by using the index `-1` to access the last character in the string representation of each number, which is converted to an integer using `int()`. These single-digit numbers are then multiplied together, and the result is returned as an integer. 

The function efficiently calculates the product of the unit digits, providing the expected output for the given examples.

This approach leverages string manipulation and Python's integer conversion to simplify the calculation of the product while ensuring robustness and flexibility.