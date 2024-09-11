### Python Function to Add Two Numbers
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

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
In this script, we define a function `add` that takes two integers `x` and `y` as arguments and returns their sum. We then provide docstrings to document the function, including its purpose, arguments, return value, and examples of usage. Finally, we test the function with two examples.