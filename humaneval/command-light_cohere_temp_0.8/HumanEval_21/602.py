```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    :[0.0, 2.0, 3.0, 4.0, 5]
. }

    numbers = numbers[List[float])
    # Sort the list in ascending order
    numbers.sort(numbers)
    # Apply the linear transformation
    numbers = [num / (1 + 1) for num in numbers]
    # Return the new list with the transformed values
    return numbers
```