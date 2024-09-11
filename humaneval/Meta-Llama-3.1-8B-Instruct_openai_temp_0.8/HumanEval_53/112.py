```python
def add(x: int, y: int):
    """
    Add two numbers x and y

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

This script defines the `add` function that takes two integers `x` and `y` and returns their sum. It also includes a docstring that explains the function's purpose, arguments, return value, and provides examples of its usage. The script then tests the function by calling it with different inputs and printing the results.