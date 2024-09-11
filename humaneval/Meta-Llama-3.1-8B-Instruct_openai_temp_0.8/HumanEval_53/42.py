### Adding Two Numbers
Here is a Python script that implements the `add` function according to the provided specification:

```markdown
### Code
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

### Explanation
This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. The function includes a docstring that provides a description of the function, its parameters, and its return value, as well as examples of how to use the function.

You can save this script to a file (e.g., `add.py`) and run it from the command line with `python add.py` to test the `add` function. 

Note: I've formatted the code according to PEP 8 for better readability. I've also used the `-> int` syntax to specify the return type of the function, which is a feature introduced in Python 3.5. If you're using an earlier version of Python, you can omit this syntax.