```python
def add(x: int, y: int):
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

# Test the function with some examples
print(add(2, 3))  
print(add(5, 7))
```

In this script, I've modified the docstring to follow the Google style guide, which is a common convention for Python docstrings. The docstring now includes a brief description of the function, the input parameters, the return value, and some example usage of the function. The function is also tested with the two examples provided in the docstring.