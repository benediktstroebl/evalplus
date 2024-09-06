Here is a self-contained Python function that solves the problem of rescaling a list of numbers to unit:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transformation to the input list to make the smallest number 0 and the largest number 1
    numbers[0] = 0
    numbers[1] = 1
    for num in numbers[2:]:
        num = (num - min(numbers)) * (1.0 / (max(numbers) - 1.0)
   0, 1)
    return numbers
```

This function takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number will become 0 and the largest will become 1. It then returns the0 list of the rescaled numbers.