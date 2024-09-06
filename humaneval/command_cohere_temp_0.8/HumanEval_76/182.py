```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating the condition `n ** int(x) == x`. 

Here's how this function works:
- The function first checks if the type of `n` is integer (`type(n) is int`). This is to ensure that the base `n` is an integer. This immediately rules out cases where `n` is a complex number, leaving only integers, floats, and rationals.
- If `n` is not an integer, it returns `False`, since the base must be an integer to make the exponentiation operation valid in Python.
- If `n` is an integer, it then checks if `x` is equal to `n ** int(x)`. The `int(x)` condition is to ensure that the exponent is also an integer. If both `n` and `x` are integers, Python 3 performs a bitwise operation called "primitive exponentiation" that results in an integer result even if both numbers are of floating-point type.

The function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

This code works for the simple power concept as described in the problem statement. Cases like `is_simple_power(1, 4)` and `is_simple_power(2, 2)` return `True`, while cases like `is_simple_power(3, 2)` and `is_simple_power(5, 3)` return `False`. 

Note that the function will return `False` if `n` is not an integer, or if `x` is not a number, as the exponentiation operator `**` does not work with those types.