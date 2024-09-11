```python
def add(x: int, y: int):
    """Add two numbers x and y
    
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

# Test the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

This script defines a function `add` that takes two integers as input and returns their sum. The docstring explains the purpose of the function, its arguments, and its return value. The script also includes two example use cases and prints the results of these examples.