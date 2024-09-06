```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    list_rescale(numbers)
    return numbers

def list_rescale(numbers):
    numbers[:] = [0.0] + numbers
   
    return [x / 100.0 for x in numbers]
```
This function takes a list of numbers and returns a new list where each number has been rescaled to the range [0,1].  The test cases for this function would involve testing whether the output of the rescale function meets the expectations for the given input.