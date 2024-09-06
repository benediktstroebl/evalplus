```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    numbers = [x / 100.0 for x in numbers]  # Apply a rescaling by dividing by 100.0 and rounding down.
    return [ numbers  # - numbers)

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers)) == [0.0, 0.0, 0.0, 1.0])
```