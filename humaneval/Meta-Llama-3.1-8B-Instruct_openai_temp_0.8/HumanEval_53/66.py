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

In this code:

*   We define a function `add` that takes two integer arguments `x` and `y`.
*   We use a docstring to document the function. The docstring explains what the function does, its input parameters, and its return value. It also includes examples of how to use the function.
*   Inside the function, we simply return the sum of `x` and `y` using the `+` operator.
*   We test the function with two example calls to demonstrate its usage.

To run this script, save it to a file (e.g., `add.py`) and execute it using Python (e.g., `python add.py`). The script will print the results of the two test calls to the console.