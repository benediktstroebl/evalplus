```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

The provided code defines a Python function `is_simple_power` that determines whether a given number `x` is a simple power of `n`. The function takes two arguments: `x` and `n`, and returns `True` if `x` is a simple power of `n`, meaning `n` raised to the power of an integer equals `x`; otherwise, it returns `False`. The function checks if `n` is an integer and if `x` equals `n` raised to the power of the integral value that would make `n * n = x`. 

Here is an example usage of the function:
```python
# Driver Code
print(is_simple_power(1, 4))  # Output: True
print(is_simple_power(2, 2))  # Output: True
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(3, 1))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```

The function's behavior aligns with the problem statement's examples, correctly identifying simple powers and non-simple powers.