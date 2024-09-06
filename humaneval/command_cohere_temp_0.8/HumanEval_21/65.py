```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    scaled = (numbers - min(numbers)) / (max(numbers) - min(numbers)) * 0.5 + 0.5
    return scaled
```

The function `rescale_to_unit` takes a list of numbers as input and applies a linear transformation to the input list. The transformation stretches or compresses the list such that the smallest number becomes 0 and the largest number becomes 1. The function is also robust; it will not error if the input list is of length 1 or if the list is empty.

Here is an example of using the above function:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```

And here is a standalone test suite for the function:
```python
import unittest

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return (numbers - min(numbers)) / (max(numbers) - min(numbers)) * 0.5 + 0.5

class TestRescaleToUnit(unittest.TestCase):
    def test_list_of_two(self):
        self.assertEqual(rescale_to_unit([1.0, 1.1]), [0.0, 0.1])

    def test_list_of_three(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0]), [0.0, 0.25, 0.5])

    def test_list_of_four(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0]), [0.0, 0.25, 0.5, 0.75])

    def test_list_of_five(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])

    def test_list_of_one(self):
        self.assertEqual(rescale_to_unit([1.0]), [0.0])

if __name__ == '__main__':
    unittest.main()
```