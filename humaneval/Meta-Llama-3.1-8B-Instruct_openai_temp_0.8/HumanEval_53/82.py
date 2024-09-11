```python
def add(x: int, y: int):
    """Add two numbers x and y

    Args:
    x (int): The first number
    y (int): The second number

    Returns:
    int: The sum of x and y

    Examples:
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

This code defines the `add` function which takes two integers as input and returns their sum. The docstring explains what the function does, its inputs, and its output. The function is then tested with two example calls.