### Python Script to Add Two Numbers
```python
def add(x: int, y: int) -> int:
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
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

In this script, the `add` function takes two integers `x` and `y` as arguments, adds them together, and returns the result. The function includes a docstring that provides documentation on how to use the function, what arguments it expects, and what it returns. The script also includes example use cases and tests the function with two different pairs of numbers.