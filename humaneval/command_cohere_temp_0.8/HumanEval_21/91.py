Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    if len(numbers) < 2:
        return numbers
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
The function `rescale_to_unit` ensures that the list passed to it has at least two elements through a type hint and a check for len(numbers) < 2. The function then calculates the minimum and maximum values in the list and divides each element in the list by the difference between the maximum and minimum values. This normalizes the list, where the smallest number becomes 0 and the largest number becomes 1. The division operation also performs a linear transformation on the numbers in the list. 
Here is an example of use for this function:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This is the result of the normalization described above.