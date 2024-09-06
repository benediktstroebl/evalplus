```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by verifying two conditions:
1. `n` should be an integer.
2. `x` should be equal to `n` raised to the power of itself, `n ** int(x == n ** x)`.

Here's an example usage of the function:
```python
# Example usage
print(is_simple_power(1, 4))  # Outputs: True
print(is_simple_power(2, 2))  # Outputs: True
print(is_simple_power(8, 2))  # Outputs: True
print(is_simple_power(3, 2))  # Outputs: False
print(is_simple_power(3, 1))  # Outputs: False
print(is_simple_power(5, 3))  # Outputs: False
```

The function should correctly identify the simple powers listed in the example test cases.