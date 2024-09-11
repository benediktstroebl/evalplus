Here's a self-contained Python script that implements the `add` function:
```markdown
# Simple Arithmetic Operations

## add Function

This script defines a function `add` that takes two integers `x` and `y` as arguments and returns their sum.

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

This script can be saved to a file (e.g., `arithmetic.py`) and run from the command line using `python arithmetic.py`. The docstring provides a clear description of the function's behavior and includes example use cases.