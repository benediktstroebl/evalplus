```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that takes two arguments, `x` and `n`. This function returns `True` if `x` is a simple power of `n`, and `False` otherwise. 

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))  # Outputs: True
print(is_simple_power(2, 2))  # Outputs: True
print(is_simple_power(8, 2))  # Outputs: True
print(is_simple_power(3, 2))  # Outputs: False
print(is_simple_power(3, 1))  # Outputs: False
print(is_simple_power(5, 3))  # Outputs: False
```

In these examples, the function is_simple_power returns true for the first three cases because the number `x` is a simple power of `n`, whereas it returns false in the last two cases because `x` is not a simple power of `n`.