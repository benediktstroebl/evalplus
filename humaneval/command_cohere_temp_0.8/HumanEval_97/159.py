```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by using the index `-1` to access the last character in the string representation of the numbers, which are converted to strings using the `str()` function. The extracted digits are then multiplied together using the `*` operator, and the result is returned as an integer using the `int()` function. 

Let's examine the example inputs provided in the problem statement:
- `multiply(148, 412)`: The unit digits are '1' and '4', respectively, resulting in the product 16.
- `multiply(19, 28)`: The unit digits are '9' and '8', respectively, resulting in the product 72.
- `multiply(2020, 1851)`: The unit digits are '0' and '8', respectively, resulting in the product 0.
- `multiply(14, -15)`: The unit digits are '4' and '-5', respectively, resulting in the product 20.

The assumption that the input is valid is stated in the problem statement. If this is not the case, unexpected behavior may occur.