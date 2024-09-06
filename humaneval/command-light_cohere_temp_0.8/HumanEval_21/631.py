```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    expected return: List[float]
    """
    # Set the min and max values to 0 and 1 respectively
    numbers = [num for num in numbers if num != 0]
    numbers.append(0)
    numbers.append(1)
    # Apply the linear transformation
    return numbers
```