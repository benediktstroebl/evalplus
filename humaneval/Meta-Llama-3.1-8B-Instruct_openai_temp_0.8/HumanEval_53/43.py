```markdown
### Add Two Numbers Function
#### Description
This script defines a function `add` that takes two integers as input and returns their sum.

#### Code
```python
def add(x: int, y: int) -> int:
    """Add two numbers x and y

    Args:
        x (int): The first number to add.
        y (int): The second number to add.

    Returns:
        int: The sum of x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y
```

#### Usage
To use this function, simply call it with two integer arguments, like this:
```python
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```
```

You can save this script to a file (e.g. `add.py`) and run it using Python (e.g. `python add.py`). Note that the docstring uses the Google Python Style Guide for documentation.