```python
def add(x: int, y: int):
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
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

This script defines a function `add` that takes two integers, `x` and `y`, and returns their sum. It also includes docstrings to provide documentation for the function and examples of how to use it. The script then tests the function with two examples.