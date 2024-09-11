### Problem Solution: Basic Addition Function

The following Python script defines a function `add` that takes two integers as input and returns their sum.

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

# Example usage:
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This function is simple, readable, and well-documented, making it easy to understand and use. The doctest strings at the top of the function provide example usage and test cases, ensuring that the function works correctly.