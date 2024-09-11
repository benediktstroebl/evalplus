```python
def add(x: int, y: int):
    """
    Add two numbers x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This code defines a function `add` that takes two integers `x` and `y` as input and returns their sum. The docstring explains the purpose of the function, its parameters, and its return value, as well as providing examples of how to use it. The function is then tested with two example calls.