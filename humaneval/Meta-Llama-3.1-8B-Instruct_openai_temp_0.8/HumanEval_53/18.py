### Adding Two Numbers in Python
Here's a self-contained Python script that calculates the sum of two numbers:

```python
def add(x: int, y: int):
    """
    Adds two numbers x and y
    
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

This script defines a function `add(x: int, y: int)` that takes two integers as arguments and returns their sum. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of usage. Two test cases are included at the end of the script to demonstrate the function's behavior.