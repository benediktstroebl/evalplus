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

print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. The docstring explains the purpose of the function and provides usage examples. The script then tests the function with two example calls and prints the results.