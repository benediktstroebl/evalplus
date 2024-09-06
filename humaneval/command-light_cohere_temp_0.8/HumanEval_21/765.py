Here is a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0
    [1.0, 0.0, 0]
    out,
    numbers = [1.0, 2.0, 3.0, 4] ** [1.0, 0]

numbers = [x / 100.0 for x in numbers]
return numbers

print(f"Rescaled list: {rescale_to_unit([1.0, 2.0, 3.0, 4])")
```