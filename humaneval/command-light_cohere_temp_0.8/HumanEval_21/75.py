Here's a self-contained Python script that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.append(x((x - 1.0 / (1.0 + numbers[0))  # Multiply by 1/sqrt(x)
    numbers = [x * y for x, y in zip(numbers, numbers[1:]))]  # Apply the same linear transform to each element of the numbers list
    return numbers
```