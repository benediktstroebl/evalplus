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

# Testing the function
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

In this script, we define a function called `add` that takes two integer arguments `x` and `y`. The function simply returns the sum of `x` and `y`. We then provide docstrings for the function to describe its purpose, arguments, return value, and provide example usage. Finally, we test the function with two example calls.