```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0, 0.0]
   
   0.0, 0]
    1)

    for idx, value in numbers:
        if idx == 0:
            numbers[idx] = 0
        elif idx == 1:
            numbers[idx] = 1
        elif idx == len(numbers) - 1:
            numbers[idx] = numbers[idx] / max(numbers)
        else:
            numbers[idx] = numbers[idx] * (1.0 / min(numbers))

    return numbers
```