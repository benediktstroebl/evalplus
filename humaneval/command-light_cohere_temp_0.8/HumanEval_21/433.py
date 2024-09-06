Here is a self-contained Python script that solves the markdown code block problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [numbers[0] / min(numbers), numbers[1:] + min(numbers)]
    return numbers
```

This function takes a list of numbers as input and returns a new list with the same values, but with the smallest number scaled down to 0 and the largest number scaled up to 1. The function uses the worth of the number in the list to scale the other numbers to a unit around 0 or 1.