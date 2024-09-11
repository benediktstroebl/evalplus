```python
def add(x: int, y: int):
    """Add two numbers x and y
    
    Args:
        x (int): The first number to be added
        y (int): The second number to be added
    
    Returns:
        int: The sum of x and y
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y

# Testing the function
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function `add(x, y)` that takes two integers `x` and `y` as input and returns their sum. It includes docstrings with explanations of the function's parameters and return value, as well as examples of how to use the function. The script also includes test cases to verify that the function works correctly.