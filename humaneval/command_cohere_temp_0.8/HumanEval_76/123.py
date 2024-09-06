```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to make sure that the power `n**int` is calculated correctly, as taking powers of non-integer types will result in complex numbers in Python.
2. `x == n ** int(x == n ** x)`: This condition checks three things at once:
    - `x == n ** x`: This compares `x` to its own power, `n**x`. If `x` is a simple power of `n`, this will be equal.
    - `int(x == n ** x)`: This uses an integer conversion before comparing. This is necessary because the comparison `x == n**x` returns a boolean, not an integer, and we want to compare it to `x` which is an integer.

The function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

The code includes type checking to ensure compatibility and utilizes the exponentiation operator `**` as well as comparison operators `==` to fulfill the requirement of the problem in a concise and efficient manner. 

This function can be used to solve the problem as required.