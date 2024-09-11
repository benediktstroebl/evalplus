```python
def add(x: int, y: int):
    """Add two numbers x and y

    Args:
        x (int): The first number
        y (int): The second number

    Returns:
        int: The sum of x and y

    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Example usage:
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. The docstring provides a description of the function, its arguments, and its return value, along with some example usage. The example usage at the end demonstrates how to call the `add` function with different inputs.