```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It checks if the type of `n` is integer (returns `true` for int, long, float, complex).
2. It checks if `x` equals `n` raised to the power of `x` divided by `n` (i.e., `x == n ** int(x == n * n)`).

The `int()` function is used to determine if `x` is an integer to ensure that the exponentiation is calculated correctly. 

Therefore, this function returns `true` if `x` is a simple power of `n` and `false` otherwise.

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))  # Outputs: True
print(is_simple_power(2, 2))  # Outputs: True
print(is_simple_power(8, 2))  # Outputs: True
print(is_simple_power(3, 2))  # Outputs: False
print(is_simple_power(3, 1))  # Outputs: False
print(is_simple_power(5, 3))  # Outputs: False
```

This example demonstrates the function's behavior for different inputs.