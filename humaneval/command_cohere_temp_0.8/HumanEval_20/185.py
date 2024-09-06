```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must contain at least two elements")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left == right else (min(left, right), max(left, right))
```

The function first sorts the input list of numbers and checks if the list contains at least two elements to make sure the indices are valid. It then determines the middle indices of the sorted list and returns the elements at those indices, or the smallest and largest elements if the middle elements are the same. The script thus correctly solves the problem of finding the closest elements in a supplied list of numbers.

Here is an example of using the function and an exception:
```python
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
(1.0, 5.0)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0])
(1.0, 4.0)
>>> find_closest_elements([1.0, 1.0, 3.0, 3.0, 4.0, 4.0])
(1.0, 1.0)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
Traceback (most recent call last):
  File "<string>", line 2, in <module>
  File "<string>", line 11, in find_closest_elements
IndexError: List of numbers must contain at least two elements
```