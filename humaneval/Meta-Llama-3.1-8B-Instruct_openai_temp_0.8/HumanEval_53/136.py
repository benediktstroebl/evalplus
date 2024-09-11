### Simple Addition Function

The following Python script defines a function `add` that adds two numbers.

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

This script defines the `add` function with type hints for `x` and `y`, indicating that they should be integers. It includes a docstring that describes the function's purpose, arguments, return value, and provides examples of how to use it. The function itself simply returns the sum of `x` and `y`. Finally, the script tests the function with two examples.