### Simple Addition Function in Python

Below is a Python script that implements the `add` function.

```markdown
# add_function.py

def add(x: int, y: int):
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


# Example usage:
print(add(2, 3))   # Output: 5
print(add(5, 7))   # Output: 12
```

This script defines a function `add(x, y)` that takes two integers as input, adds them together, and returns the result. The docstring for this function provides documentation on what the function does, its input parameters, and its return value. The script also includes example usage of the `add` function.