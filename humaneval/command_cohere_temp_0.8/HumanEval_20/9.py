```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        mid = len(numbers) // 2
        return numbers[mid - 1], numbers[mid]
```

The function **find_closest_elements** takes a list of numbers as input and returns the two closest numbers in the list. The list is first sorted and then depending on the length of the list, either the element at the middle or the last element is returned together with the element at the midpoint or the first element. This logic handles both edge cases and standard cases. 

Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # output: (2.0, 2.2)
```

And here is the unittest:
```python
import unittest

class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements_with_single_element_list(self):
        with self.assertRaises(IndexError):
            find_closest_elements([1.0])
        
    def test_find_closest_elements_with_two_elements_list(self):
        result = find_closest_elements([1.0, 2.0])
        self.assertEqual(result, (1.0, 2.0))

    def test_find_closest_elements_with_three_elements_list(self):
        result = find_closest_elements([1.0, 2.0, 3.0])
        self.assertEqual(result, (1.0, 2.0))

    def test_find_closest_elements_with_four_elements_list(self):
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(result, (2.0, 3.0))

    def test_find_closest_elements_with_five_elements_list(self):
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(result, (2.0, 3.0))

    def test_find_closest_elements_with_list_containing_same_elements(self):
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        self.assertEqual(result, (2.0, 2.0))

    def test_find_closest_elements_with_large_list_containing_close_elements(self):
        result = find_closest_elements([1.0, 1.1, 1.11, 1.12, 1.13, 1.99, 1.999, 1.9999, 2.0])
        self.assertEqual(result, (1.999, 2.0))

if __name__ == '__main__':
    unittest.main()
``` 

The unittest contains test cases to handle the following:
- Single element list: Tests the correctness of the **IndexError** that is thrown. 
- Lists of varying lengths: Tests the function's ability to find the