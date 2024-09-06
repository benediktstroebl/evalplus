Here's a self-contained Python script that solves the problem of applying a linear transformation to a list of numbers in markdown code block:

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    return [0.0, 1.0, 0.5]

```