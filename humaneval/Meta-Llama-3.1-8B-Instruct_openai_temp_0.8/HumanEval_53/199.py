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

print(add(2, 3))
print(add(5, 7))
```

In this script, we define a function `add` that takes two integers `x` and `y` as arguments and returns their sum. We then call this function with the arguments `(2, 3)` and `(5, 7)` and print the results. 

The docstring for the `add` function includes a description of what the function does, a list of the arguments it takes, and a description of the result it returns. The examples are included as doctest strings, which can be run using the `doctest` module to verify that the function behaves correctly.