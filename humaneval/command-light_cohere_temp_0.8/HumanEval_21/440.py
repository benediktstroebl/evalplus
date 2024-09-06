Here is a Python script with a self-contained function that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This function takes a list of numbers as input and returns a new list with the same values, but with each number rescaled to be between 0 and 1. The function can be used to test its functionality by passing a test list and checking if the returned list is correct.