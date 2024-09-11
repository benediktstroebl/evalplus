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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. It includes a docstring that describes the function's behavior, including its input arguments and return value, as well as examples of how to use the function. The script also includes two test calls to the function to demonstrate its behavior.