Here's a self-contained Python script with a function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Rescale list of numbers to have 0 at the minimum and 1 at the maximum.
    return [numbers[ (numbers, lambda x: x > 1.0, lambda x: x < 0.0)[:-1]]
```

This function, rescale_to_unit, takes a list of numbers and returns a new list where each number has been rescaled to be between 0 and 1. It uses the lambda functions to define the conditions for the rescaling. 
This function effectively stretches the range of numbers so that they are within the [0,1] range, and it ensures that the numbers become positive.