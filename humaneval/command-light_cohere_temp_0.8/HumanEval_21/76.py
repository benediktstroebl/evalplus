```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [n / 100.0 for n in numbers]  # Rescale each element to [0,1]
    return numbers

# Test case
input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
return rescale_to_unit(input_numbers)
```