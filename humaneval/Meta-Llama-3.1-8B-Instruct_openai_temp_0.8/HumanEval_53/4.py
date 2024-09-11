```python
def add(x: int, y: int):
    """Add two numbers x and y

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

In this code:

- We define a function `add` that takes two parameters `x` and `y`, both of type `int`.
- The function returns the sum of `x` and `y`.
- We include docstrings to provide documentation about the function, including its parameters, return value, and examples of usage.
- The examples are tested using doctests, which can be run using the `python -m doctest` command.

You can save this code to a file (e.g., `add.py`) and run it from the command line using `python -m doctest add.py` to test the doctests.