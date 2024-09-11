### Simple Addition Function

```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

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

This code defines a simple function `add` that takes two integers `x` and `y` as arguments and returns their sum. It includes a docstring that describes the function's behavior, its parameters, and its return value. The example usage at the end demonstrates how to use the function.