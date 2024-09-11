### Python Script for Adding Two Numbers
```python
def add(x: int, y: int) -> int:
    """
    Adds two numbers x and y.

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
This script defines a function `add` that takes two integers `x` and `y` as arguments and returns their sum. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of usage. The script also includes two test cases to verify the function's correctness.