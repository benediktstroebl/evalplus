```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y
    
    Args:
        x (int): The first number to add.
        y (int): The second number to add.
    
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

This script defines a function `add(x, y)` that takes two integer arguments and returns their sum. The docstring provides documentation for the function, including a description, argument and return type information, and examples of usage. The script then tests the function with two example calls.