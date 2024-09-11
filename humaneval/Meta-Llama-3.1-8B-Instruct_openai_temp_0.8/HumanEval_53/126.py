### Basic Arithmetic Operation: Addition
#### `add` Function
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

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
You can save this script to a file (e.g., `add.py`) and run it from the command line using Python (e.g., `python add.py`).

Alternatively, you can run the doctests included in the docstring using the following command:
```bash
python -m doctest add.py
```