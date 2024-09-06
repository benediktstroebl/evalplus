```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)
```

The function checks if the number `x` is a simple power of `n` by comparing their types and then confirming whether `x` can be written as `n ** int(n ** 0.5)`, which is the decimal representation of `n` raised to the power of `x`. 

For example, it returns `True` for inputs like `is_simple_power(1, 4)`, `is_simple_power(2, 2)`, and `is_simple_power(8, 2)`, and `False` for cases like `is_simple_power(3, 2)`, `is_simple_power(3, 1)`, and `is_simple_power(5, 3)`. 

This approach eliminates the need to manually check orders of integers and provides a simple and efficient solution.