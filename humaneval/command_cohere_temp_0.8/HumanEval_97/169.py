```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by using the index `-1` to access the last character in the string representation of the numbers, which are converted to strings using the `str()` function. The extracted digits are then multiplied together using the `*` operator, and the result is returned as an integer. 

The assumption that the input is valid overlooks potential issues with the input values. This function assumes that both input values are valid integers. If the input values are not valid, there may be errors. However, for the given examples, the function will work as expected.