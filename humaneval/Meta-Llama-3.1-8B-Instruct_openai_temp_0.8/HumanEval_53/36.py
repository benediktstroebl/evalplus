```python
def add(x: int, y: int):
    """
    This function takes two integers as input and returns their sum.

    Args:
        x (int): The first number to add.
        y (int): The second number to add.

    Returns:
        int: The sum of x and y.

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

This script defines a function `add` that takes two integers `x` and `y`, adds them together using the `+` operator, and returns the result. The function is then tested with two example calls, which print the expected results to the console.