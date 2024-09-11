```python
def add(x: int, y: int) -> int:
    """
    This function adds two numbers x and y.

    Args:
        x (int): The first number to be added.
        y (int): The second number to be added.

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

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. It includes docstrings to provide documentation and examples of usage, as well as test cases to verify the function's correctness.