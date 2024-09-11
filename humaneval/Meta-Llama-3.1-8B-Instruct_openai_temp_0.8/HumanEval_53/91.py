```markdown
### Python Function to Add Two Numbers
#### Code

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

#### Usage

To use this function, simply call `add` with two integer arguments, like this:

```python
result = add(2, 3)
print(result)  # Output: 5
```

#### Testing

You can test the function with the provided doctests using the `unittest` module:

```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```

Run this script to see the test pass.
```