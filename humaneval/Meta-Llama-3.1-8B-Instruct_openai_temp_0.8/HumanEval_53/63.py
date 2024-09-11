### Adding Two Numbers in Python
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
You can run this script in your Python environment to test the `add` function.

To test the function, you can use a Python interpreter or a testing framework like `unittest`. Here's an example using `unittest`:

```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```

You can also use the `doctest` module that comes with Python's standard library to automatically test the docstrings:

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

def main():
    doctest.testmod()

if __name__ == "__main__":
    main()
```