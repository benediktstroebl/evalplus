```python
def add(x: int, y: int):
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

    Returns:
        int: The sum of x and y

    Example:
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

This script is self-contained and includes:

- A function called `add` that takes two integers `x` and `y` as arguments and returns their sum.
- A docstring that includes a description of the function, its arguments, return value, and example usage.
- Two test calls to the `add` function to demonstrate its usage.