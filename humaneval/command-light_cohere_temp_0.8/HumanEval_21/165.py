Here's the self-contained Python script with the requested function:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Assuming that the list has at least 2 elements
    numbers = [min(numbers), max(numbers)] + [numbers[1] - numbers[0]]
    return numbers
```