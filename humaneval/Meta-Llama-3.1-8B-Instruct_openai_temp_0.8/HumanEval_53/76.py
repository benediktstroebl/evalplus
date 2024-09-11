```python
def add(x: int, y: int) -> int:
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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function `add` that takes two integers as input and returns their sum. The function includes a docstring that explains what it does, its parameters, and its return value. The script also includes two test cases to demonstrate the function's usage.