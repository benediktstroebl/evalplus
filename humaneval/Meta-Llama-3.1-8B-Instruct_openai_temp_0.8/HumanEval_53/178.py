Here is a Python script that implements the `add` function:
```markdown
# Add two numbers
=====================================

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

    Args:
        x (int): The first number to add
        y (int): The second number to add

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

You can use this function as follows:

```python
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

To test the function, you can run this script using Python. The `>>>` symbols in the docstring are used to indicate a Python prompt. When you run this script, it will execute the functions and print the output.