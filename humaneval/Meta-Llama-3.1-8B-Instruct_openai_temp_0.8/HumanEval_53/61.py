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
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This script defines a function `add` that takes two integers `x` and `y` as arguments, returns their sum, and includes documentation with examples using the `doctest` module. When run, it will print the results of the function calls to verify the correctness of the function.