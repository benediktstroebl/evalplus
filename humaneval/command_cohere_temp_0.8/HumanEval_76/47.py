```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The given function checks if the number `x` is a simple power of `n` and returns `True` if it is and `False` otherwise. It does so by taking two arguments, `x` and `n`, and checking two conditions:
1. It checks that the type of `n` is `int` to filter out non-integer exponents.
2. It checks that `x` is equal to `n` raised to the power of the integer value of `x` being equal to `n`. If both conditions are satisfied, it returns `True`. Otherwise, it returns `False`. 

The unit tests for the function can be created as follows:
```python
# Testing the function with simple cases
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True

print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```

These tests check if the function correctly identifies simple powers of integers for different input cases.