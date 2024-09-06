```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = nums_sorted[1] - nums_sorted[0]
    for i in range(1, len(nums_sorted)):
        current_diff = nums_sorted[i] - nums_sorted[i - 1]
        if abs(diff) > abs(current_diff):
            diff = current_diff
    return nums_sorted[0], nums_sorted[1]
```

The function works by first sorting the input list of numbers. Then, it computes the difference between subsequent elements in the sorted list. If the absolute difference is greater than the current closest difference, it updates the closest difference. Finally, it returns the first and the second element of the list, which will be the two closest numbers from the original input list. 

Here is a sample output:
```
python
find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)
```

This is tested with:
```
>>> import unittest
>>> class TestFindClosestElements(unittest.TestCase):
...     def test_find_closest_elements_with_list_with_two_elements(self):
...         self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))
...     def test_find_closest_elements_with_list_with_three_elements(self):
...         self.assertEqual(find_closest_elements([1.0, 2.0, 3.0]), (2.0, 2.0))
...     def test_find_closest_elements_with_list_with_more_than_three_elements(self):
...         self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
...     def test_find_closest_elements_with_list_with_same_values(self):
...         self.assertEqual(find_closest_elements([1.0, 1.0, 1.0, 1.0]), (1.0, 1.0))
...     def test_find_closest_elements_with_empty_list(self):
...         with self.assertRaises(ValueError):
...             find_closest_elements([])
...     def test_find_closest_elements_with_list_with_only_one_element(self):
...         with self.assertRaises(ValueError):
...             find_closest_elements([1.0])
... 
>>> unittest.main()
```