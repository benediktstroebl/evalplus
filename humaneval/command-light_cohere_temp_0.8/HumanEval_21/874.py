```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input: numbers: list of float
    Output: list of float
    """
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test case
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_rescale_number = rescale_to_unit(input_list)
print(test_rescale_number)
```