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
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return x + y
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of its usage. The docstring is written in the Google Style, which is a common convention for Python documentation. If either `x` or `y` is not an integer, the function raises a `TypeError`.