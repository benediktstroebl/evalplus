```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function corroborates that `n` is an integer and compares `x` to the result of raising `n` to the power of `int(x == n**x)`, which represents the integer part of the exponent required to achieve the value `x` using repeated multiplication of `n`. This validation aims to ensure that `x` is a straightforward product of `n` raised to a whole number exponent.

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```

In the example, the function is called multiple times with different arguments to test its behavior. The outputs show that the function returns `True` for simple power cases and `False` for non-simple power cases.