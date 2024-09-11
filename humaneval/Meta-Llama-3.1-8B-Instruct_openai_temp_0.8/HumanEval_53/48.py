### Basic Arithmetic Addition Function in Python

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
print(add(2, 3))
print(add(5, 7))
```

This script defines a function `add` that takes two integers `x` and `y` and returns their sum. The function includes a docstring that provides documentation, including the function's purpose, input arguments, return value, and examples of usage. The script then tests the function with two example cases.