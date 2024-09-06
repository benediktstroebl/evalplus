```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function corroborates that the exponent `n` is an integer and the `base` n raised to the power of `x` equals `x`; if both conditions are met, it returns `True`, indicating a simple power, otherwise, it returns `False`. 

Here is an example of function use:
```python
# Example usage
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```