### Adding Two Numbers
#### Problem Statement
The task is to write a Python function that takes two integers as input and returns their sum.

#### Solution
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

#### Explanation
The `add` function takes two integers `x` and `y` as input and returns their sum using the `+` operator. The docstring provides a description of the function, its arguments, return value, and includes example use cases.

#### Usage
To use this function, simply call it with two integers, like this:
```python
result = add(2, 3)
print(result)  # Output: 5
```