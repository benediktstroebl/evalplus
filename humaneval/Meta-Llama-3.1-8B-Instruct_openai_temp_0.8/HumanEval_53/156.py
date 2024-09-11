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
if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```

This script defines a function called `add` that takes two integer arguments `x` and `y`, adds them together, and returns the sum. The docstring for the function explains its purpose, arguments, return value, and provides example usage. The script also includes a test section at the end to demonstrate the function's behavior.