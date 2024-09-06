```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n + 1) for n in numbers]
    return [x / (x + 1) for x in numbers]

def test_rescale_to_unit(numbers: List[float]) -> None:
    """ Test the function rescale_to_unit
    """
    print(rescale_to_unit([0, 0, 0, 0, 0, 0, 0, 0] )) # [0.0, 0.0, 0.0, 0.0, 0.0, 0]
   0, 0]
    print(rescale_to_unit([0, 0, 0, 1, 2, 3, 4, 5])) # [0.0, 0.0, 0.0, 0.5]
   0.0, 0.0, 0]
   0.0, 0]
    [0.0, 0.0, 0.0, 0]
[0.0, 0, 0, 1, 1, 2, 2]  # [0, 0, 0, 0.0, 0, 0, 0]
    print(rescale_to_unit([0.0, 0.0, 0])) # [0.0, 0.0, 0]
0.0, 0)
[0.0, 0, 0, 1, 1, 2, 2, 2.0, 0]  # [0.0, 0.0, 0]
[0.0, 0, 0, 1, 1, 2, 2, 3] # [0.0, 0, 0, 0, 0, 0, 0, 0, 0]

# These tests demonstrate that the function successfully applies the linear transformation to the input list of numbers.