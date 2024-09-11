### Adding Two Numbers in Python
#### Script

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

# Test the function with the provided examples
assert add(2, 3) == 5
assert add(5, 7) == 12

# Test the function with additional examples
assert add(-5, 3) == -2
assert add(0, 0) == 0
assert add(-1, 1) == 0
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. It includes docstrings that describe the function's behavior, its input and output types, and provide examples of how to use the function. The script also includes assertions to test the function with various inputs.