### Python Script: Simple Addition Function
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

    Args:
        x (int): The first number to add.
        y (int): The second number to add.

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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```
This script defines a simple `add` function that takes two integers as input and returns their sum. The function includes a docstring with a description, example usage, and type hints for the input and output parameters. The script also includes two example usage lines to demonstrate how to use the function.