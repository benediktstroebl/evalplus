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
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

This script defines a function `add(x, y)` that takes two integers as input and returns their sum. The function includes docstrings to provide documentation and example usage. The script then tests the function with two example inputs.