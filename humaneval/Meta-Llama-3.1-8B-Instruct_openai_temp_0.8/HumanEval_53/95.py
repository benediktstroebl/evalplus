```python
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Test the function
print(add(2, 3))    # Output: 5
print(add(5, 7))    # Output: 12
```

This script defines a function `add` that takes two integers `x` and `y` as input and returns their sum. It includes docstrings with example usage to describe the function's behavior. The script then tests the function with two different input pairs. 

However, the `>>>` syntax is usually used for doctests which are not run when the script is executed. If you want to automatically test the function when the script is run, you can use the `unittest` module. Here's how you could modify the script to use `unittest`: 

```python
import unittest

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```

This version of the script uses a test class `TestAddFunction` with a single method `test_add` that checks the function's behavior with two different input pairs. The `unittest.main()` function is only called when the script is run directly, not when it's imported as a module.