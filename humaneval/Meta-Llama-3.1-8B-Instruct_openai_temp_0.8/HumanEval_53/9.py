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

In this script, I've improved the docstring to include a clear description of the function, its parameters, and its return value. I've also added more informative docstring examples. The function itself remains the same, simply returning the sum of `x` and `y`. The script also includes test cases at the end to verify that the function works as expected.