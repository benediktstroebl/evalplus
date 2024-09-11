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

# Test the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

However, for Docstrings & Testing, it is better to use the `unittest` module in Python, here is how you could write the same code:

```python
import unittest

def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number
        y (int): The second number

    Returns:
        int: The sum of x and y
    """
    return x + y

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-5, 7), 2)

if __name__ == '__main__':
    unittest.main()
```

You can run this script, and it will automatically run the tests and display the results.