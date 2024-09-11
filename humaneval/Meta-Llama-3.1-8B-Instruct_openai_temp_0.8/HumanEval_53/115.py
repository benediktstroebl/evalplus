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
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. It includes a docstring that describes the function's behavior, its arguments, return values, and provides examples of how to use the function. Finally, it tests the function with some example calls.