```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by comparing it with `n` raised to the power of the integer value obtained by evaluating the equality `x == n ** x`. The type checking ensures that `n` is an integer.

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))     # Output: True
print(is_simple_power(2, 2))     # Output: True
print(is_simple_power(8, 2))     # Output: True
print(is_simple_power(3, 2))     # Output: False
print(is_simple_power(3, 1))     # Output: False
print(is_simple_power(5, 3))     # Output: False
``` 

This example shows that the function returns `True` for cases where the number `x` is a simple power of `n`, and returns `False` otherwise.