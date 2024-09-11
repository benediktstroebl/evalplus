### Adding Two Numbers
#### Problem Description
The following Python script defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

#### Code
```python
def add(x: int, y: int):
    """
    Add two numbers x and y

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

#### Explanation
This script defines a function `add` that takes two arguments `x` and `y` of type `int`. The function simply returns the sum of `x` and `y`. The docstring provides a description of the function, its arguments, return value, and some examples of how to use it. The script includes two test cases at the end to ensure the function works correctly.