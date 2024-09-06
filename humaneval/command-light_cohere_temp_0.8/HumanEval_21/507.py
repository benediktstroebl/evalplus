```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
    numbers: List[float] - list of numbers
    Returns:
    List[float] - list of numbers after applying the transformation
    """
    numbers[0] = 0
    numbers[1] = 1
    return numbers

# Example test cases:
# Given list of numbers: [1.0, 2.0, 3.0, 4.0, 5]

result:
[0.0, 0.0, 0.0, 0]

Test case 2:
[0.75, 0.0, 0]
result:
[0.75, 0, 0]

Test case 3:
[-4.75, -4.75, -4.75]
result:
[0, 0, 0]

Test case 4:
[0, 0, 0, 0]

result:
[0, 0, 0, 0]

Test case 5:
[-1.0, 0, 0, 0]

result:
[-1.0, 0, 0, 0]

Test case 6:
[1.0, 2.0, 3.0]
result:
[0.0, 0.0, 0]

Test case 7:
[10.0, 1, 2]

result:
[10.0, 10.0, 20]

Test case 8:
[-100.0, -100.0, -100.0]
result:
[-100.0, 0, 0]
```