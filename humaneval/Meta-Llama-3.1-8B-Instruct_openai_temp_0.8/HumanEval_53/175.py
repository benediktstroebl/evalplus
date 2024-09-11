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
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

However, if you want to stick with the original example's docstring formatting, here's the revised script:

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
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

This script defines a function `add` that takes two integer arguments, adds them, and returns the result. The docstring provides a description of the function, its arguments, return value, and some example use cases. The script also includes some test cases at the end to demonstrate the function's behavior.