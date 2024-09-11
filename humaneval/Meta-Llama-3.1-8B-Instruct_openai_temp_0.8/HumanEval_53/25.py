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

This script defines the `add` function to calculate the sum of two integers, and includes a docstring to document the function's behavior, parameters, and return value. It also includes test cases to verify the function's correctness.