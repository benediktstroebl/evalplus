```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
    x (int): The first number
    y (int): The second number

    Returns:
    int: The sum of x and y

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

In this script, I've modified the original function to include a type hint for the return value, and I've added a docstring to describe the function's behavior. The docstring includes a description of the function, its arguments, and its return value, as well as some example use cases. I've also added two print statements to test the function.