```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Assertions:
    assert len(numbers) >= 2
    assert all(isinstance(number, (int, float)) for number in numbers)

    # Apply linear transformation
    transformed_numbers = [0 if number == 0 else number for number in numbers]

    return transformed_numbers
```