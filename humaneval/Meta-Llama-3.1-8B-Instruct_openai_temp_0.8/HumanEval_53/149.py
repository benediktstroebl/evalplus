```markdown
### Addition Function

#### Description
A simple function that adds two numbers.

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

#### Usage
To use this function, simply call it with two integers as arguments, like this:
```python
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```

#### Notes
This function uses Python's built-in type hinting to specify that `x` and `y` should be integers. It also includes a docstring that provides a brief description of the function, its arguments, return value, and some examples of usage. The examples are written in a format that can be read by tools like doctest, which is a built-in Python module for testing code using examples.
```