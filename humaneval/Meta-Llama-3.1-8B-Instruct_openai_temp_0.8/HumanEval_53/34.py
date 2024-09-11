### Add Two Numbers
#### Problem Description
This script defines a function `add(x: int, y: int)` that takes two integers as input and returns their sum.

#### Code
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
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

#### Explanation
This script defines a function `add(x: int, y: int)` that calculates the sum of two integers `x` and `y`. The function uses the `return` statement to output the result. The docstring provides a description of the function, its arguments, return value, and examples of how to use it. The test at the end of the script prints the result of calling `add(2, 3)` and `add(5, 7)` to ensure the function works as expected.