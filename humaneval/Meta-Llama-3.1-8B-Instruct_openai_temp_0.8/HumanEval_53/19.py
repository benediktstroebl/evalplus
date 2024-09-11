### Adding Two Numbers in Python
#### Description
This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

#### Code
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
```

#### Usage
You can use this function by calling it with two integers as arguments, like this:
```python
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```