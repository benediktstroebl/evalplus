```python
def add(x: int, y: int):
    """Add two numbers x and y

    Args:
        x (int): The first number to be added
        y (int): The second number to be added

    Returns:
        int: The sum of x and y

    Example:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y

# Testing the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

This script defines a function `add` that takes two integers `x` and `y` as arguments and returns their sum. The function is documented with a docstring that explains its purpose, parameters, return value, and provides examples of its usage. The script then tests the function with a couple of examples.