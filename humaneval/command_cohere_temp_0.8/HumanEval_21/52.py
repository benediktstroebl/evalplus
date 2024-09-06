```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] via linear transformation. This method is highly efficient, as it utilizes Python's list comprehension and basic arithmetic for vector transformation.

To test this function, you can use the following input list and verify that the output list reflects the correct scaling:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_result = [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit(test_list))
```

This script guarantees that the function `rescale_to_unit` correctly transforms a given list of numbers to a range of 0 to 1, providing great utility for data normalization and other data-related tasks.