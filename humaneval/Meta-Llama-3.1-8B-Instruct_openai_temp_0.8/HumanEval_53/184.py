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

This script defines a function `add` that takes two integers `x` and `y` as arguments and returns their sum. The docstring provides a description of the function, its arguments, return value, and some examples of how to use it. The `>>>` notation is used to indicate expected output in the doctest examples. 

To run the doctest, save this script to a file (e.g., `add.py`) and execute it using the following command:

```bash
python -m doctest add.py
```

This will run the doctest and print any failures to the console.