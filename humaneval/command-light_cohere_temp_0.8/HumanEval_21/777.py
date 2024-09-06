Here is a Python script that includes a self-contained function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    """
    numbers[0] = 0
    numbers[1] = 1
    return numbers

# Test the function
# Example input list [1.0, 2.0, 3.0, 4.0, 5.0]
array numbers = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])

expected output is [0.0, 0.0, 1.0, 1.0]
```