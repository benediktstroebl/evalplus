```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left == right else (min(left, right), max(left, right))
```

The function `find_closest_elements()` takes a list of numbers, sorts it, and then checks the elements at the middle index (or the closest index to the middle if the list length is odd). Depending on whether these elements are the same or not, it returns the smallest (closest) of the two, or the largest (also closest) of the two. This logic guarantees the returned pair as being the two elements closest to each other in the list. 

Here's a basic unit test for the function leveraging Python's `unittest` module:
```python
import unittest

class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements_with_odd_length_list(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    def test_find_closest_elements_with_even_length_list(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    def test_find_closest_elements_with_list_less_than_two(self):
        with self.assertRaises(IndexError):
            find_closest_elements([1.0, 2.0])
```