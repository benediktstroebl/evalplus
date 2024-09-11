```python
def add(x: int, y: int) -> int:
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

In this script, the `add` function takes two integers `x` and `y` as input and returns their sum. The docstring provides a description of the function, its parameters, and its return value, along with some examples of how to use it. The last two lines of the script test the function with the given examples.