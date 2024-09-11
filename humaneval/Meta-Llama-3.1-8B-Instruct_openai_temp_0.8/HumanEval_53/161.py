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

In this script, we define a function `add` that takes two integers `x` and `y` as arguments and returns their sum. The function includes a docstring that provides a description, explains the function's arguments and return values, and includes some example use cases. Finally, we test the function with some example inputs to demonstrate its behavior.