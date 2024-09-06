```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
This Python function uses the built-in `max` function to determine the maximum element in the provided list `l`, and subsequently returns it. As seen in the examples, the function handles both positive and negative numbers gracefully, opting for the highest value in either scenario. 
The test examples are also provided to confirm function accuracy. 
To run the test, you can use Python's built-in `unittest` module:
```python
import unittest

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()
```

This will run the test and indicate if it passes or fails.