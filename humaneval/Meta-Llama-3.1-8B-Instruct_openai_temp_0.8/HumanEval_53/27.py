```python
def add(x: int, y: int):
    """Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

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

This script defines a function `add` that takes two integers as input and returns their sum. The function includes a docstring that provides documentation for the function, including its arguments, return value, and examples of usage. The script also includes two test cases to verify that the function works as expected.