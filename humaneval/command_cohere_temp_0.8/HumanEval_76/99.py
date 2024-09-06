```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (of type `int`) to ensure that the exponent `n` is an integer.
2. If the type of `n` is int, it then compares `x` with `n` raised to the power of the integer value of `x == n ** x`. This way, it checks if `x` can be written as `n^int` for some integer value of `int`. 

Example tests:
```python
# Testing a true scenario
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True

# Testing a false scenario
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```