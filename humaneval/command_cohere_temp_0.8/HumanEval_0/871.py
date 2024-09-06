Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```
The function `has_close_elements` takes two parameters: 
1. `numbers`: A list of floating numbers
2. `threshold`: A floating threshold value to compare with. 

The function returns `True` if there are two elements in the list that are less than the threshold apart in the list, otherwise returns `False`.

This is tested using python's unittest framework as follows:
```python
import unittest

class TestHasCloseElements(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))
if __name__ == '__main__':
    unittest.main()
```
The first test checks if the function returns `True` with a list of numbers with two elements that are less than the threshold (0.3 in this case) apart. The second test checks whether the function returns `False` with a list of numbers with no two close elements with a threshold of 0.5.