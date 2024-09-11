### Self-Contained Python Script for Basic Addition Function

Below is a Python script that includes a function `add` for adding two numbers. The function includes a docstring for documentation and uses doctest to verify its functionality.

```python
import doctest

def add(x: int, y: int):
    """
    Add two numbers x and y
    
    Args:
        x (int): The first number.
        y (int): The second number.
    
    Returns:
        int: The sum of x and y.
    
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

To use this script, simply save it to a Python file (e.g., `addition.py`), navigate to the directory containing the file in your command prompt or terminal, and run `python addition.py`. The `doctest` module will automatically test the `add` function with the examples provided in the docstring.