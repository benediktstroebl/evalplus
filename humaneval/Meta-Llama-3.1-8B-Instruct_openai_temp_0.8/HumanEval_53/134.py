### Adding Two Numbers in Python
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

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
This script defines a function `add` that takes two integers, `x` and `y`, and returns their sum. The function includes docstrings to provide documentation and examples of usage. The script also includes test cases to verify the function's correctness.