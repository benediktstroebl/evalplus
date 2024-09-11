### Adding Two Numbers
#### Python Function to Add Two Integers

```python
def add(x: int, y: int) -> int:
    """
    This function adds two integers x and y.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The sum of x and y.

    Example:
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

This script defines a function `add` that takes two integers `x` and `y` as arguments, adds them together, and returns their sum. It includes docstrings with example usage to provide context and clarity. The example usage at the end demonstrates how to call the `add` function with different input values.