```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t."""
    return all(num < t for num in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list `l` and an integer `t` as input, and returns `True` if all numbers in the list are below the threshold `t`, and `False` otherwise. The `all` function is used with a generator expression to check this condition. The script then includes two test cases to demonstrate the function's behavior.