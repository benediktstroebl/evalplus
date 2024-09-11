```python
def add(x: int, y: int) -> int:
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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

In this script, the `add` function takes two integers `x` and `y`, adds them together, and returns the result. The function includes a docstring that describes its purpose, parameters, return value, and provides example use cases. The script also includes two test cases to verify that the function works correctly.