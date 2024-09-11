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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function called `add` that takes two integer arguments, `x` and `y`, and returns their sum. It also includes docstrings to document the function, including its arguments, return value, and examples of how to use it. Finally, it tests the function with two example calls.