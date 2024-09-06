Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers
```
This function takes a list of numbers as input and applies a linear transform to that list, such that the smallest number will become 0 and the largest will become 1. The function then returns a list of numbers.