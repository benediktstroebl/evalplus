```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t."""
    return all(i < t for i in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines the `below_threshold` function, which takes a list `l` and an integer `t` as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in `l` are below `t`. The function returns `True` if this condition is met, and `False` otherwise. The test cases demonstrate the function's behavior.