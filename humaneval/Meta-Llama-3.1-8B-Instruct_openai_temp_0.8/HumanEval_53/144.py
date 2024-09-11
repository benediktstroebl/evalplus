### Add Two Numbers
#### Problem Statement

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

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
```

#### Explanation

This function uses the built-in `+` operator in Python to add the two input numbers `x` and `y` and returns the result.

#### Usage

To use this function, simply call it with two integers as arguments, like this:
```python
result = add(2, 3)
print(result)  # Output: 5
```