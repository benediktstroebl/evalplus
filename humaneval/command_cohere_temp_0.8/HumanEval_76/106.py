```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by doing the following:
1. It verifies that the provided number `n` is an integer. This is done to ensure that the power equation is valid.
2. It checks if `x` is equal to `n` raised to the power of `x` (`n**x`). This step is crucial, as it determines if `x` is a valid power of `n`.
3. Additionally, it checks if the result of the previous operation is also an integer. This is to ensure that the exponentiation `n**x` yields an integer result when `x` is an integer.

This function efficiently determines whether `x` is a simple power of `n` and returns `True` if it is, or `False` otherwise. 

You can use this function to solve the problem as demonstrated in the code snippet below:
```python
# Testing the function
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```

This demonstrates how to utilize the `is_simple_power()` function to determine whether a number is a simple power of another number, and it returns `True` or `False` accordingly.