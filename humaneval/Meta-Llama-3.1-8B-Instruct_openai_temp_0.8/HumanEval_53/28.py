```python
def add(x: int, y: int) -> int:
    """Add two numbers x and y

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

In this script, we define a function `add` that takes two integer arguments, adds them together, and returns the result. We also include docstrings to document the function's behavior, including its arguments, return value, and examples of usage. Finally, we test the function with some sample inputs to demonstrate its correctness.