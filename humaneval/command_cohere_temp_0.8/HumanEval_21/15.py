Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    return [(x-min(numbers))/(max(numbers)-min(numbers)) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. You can test this function by calling it with a list of at least two numbers, like this:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This output is expected due to the fact that the largest number in the list ([5.0]) becomes 1.0, and the smallest number in the list ([1.0]) becomes 0.0, with each other number being a linear combination of these two extremes.