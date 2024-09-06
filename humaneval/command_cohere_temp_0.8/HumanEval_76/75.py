```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function leverages the nature of exponential growth to determine if `x` is a power of `n`, and the result is delivered via the returned boolean value. This approach ensures that the function efficiently identifies simple power relationships between the given numbers.