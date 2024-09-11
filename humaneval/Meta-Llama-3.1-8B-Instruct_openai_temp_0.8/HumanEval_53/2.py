```python
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Test the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

This script defines the `add` function with a docstring to describe its purpose and includes doctests to verify its correctness. The function simply returns the sum of its two integer arguments. The script then tests the function with the two doctests provided.