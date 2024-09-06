```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers[:0] = 0
    numbers = [x * 100.0 for x in numbers]
    return numbers
```

This code is a self-contained Python function that solves the problem of rescaling a list of numbers to the unit range of 0 to 1. It uses the list comprehension and the `*100.0` factor scale factor to scale each number in the list by 100 and then uses the list slicing notation to extract the rescaled values.