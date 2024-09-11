### Self-Contained Python Script
```python
"""
A simple Python script that defines a function to add two numbers.
"""

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

# Example usage:
print("5 + 7 =", add(5, 7))
```
This script defines a function `add` that takes two integers as input and returns their sum. The example usage at the end demonstrates how to use the function to add two numbers.