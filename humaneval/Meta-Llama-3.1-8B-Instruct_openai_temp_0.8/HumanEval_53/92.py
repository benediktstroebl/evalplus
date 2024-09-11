### Python Add Function
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

To use this function, save it to a file (e.g., `add.py`) and run it with Python:
```bash
python add.py
```
This will load the function and allow you to test it with the examples provided.

Alternatively, you can execute the function directly in a Python interpreter:
```python
$ python
>>> from add import add
>>> add(2, 3)
5
>>> add(5, 7)
12
```
This will load the function and allow you to test it interactively.