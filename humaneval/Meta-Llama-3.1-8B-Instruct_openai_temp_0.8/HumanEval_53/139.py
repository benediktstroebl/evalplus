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

You can run this script in your Python environment to test the function. 

However, keep in mind that Python's built-in `doctest` module can automatically test the function based on the docstring. If you want to use `doctest` module, you should run the script with the `-v` option. For instance, `python -m doctest -v script.py`. 

Here's a full example:

```python
import doctest

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

if __name__ == "__main__":
    doctest.testmod()
```