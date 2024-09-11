### Add Two Numbers Function
#### A simple Python function to add two numbers.

```python
def add(x: int, y: int) -> int:
    """
    This function adds two numbers x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

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

This script defines a function `add` that takes two integer arguments `x` and `y` and returns their sum. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of its usage. The script also includes test cases to demonstrate the function's correctness.