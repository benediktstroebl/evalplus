```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0, 0]
    for i in numbers:
        numbers[i] = 1.0 * (numbers[i] / max(numbers)) + 0.0
   
    result = [0.0] if numbers[max] == 0 else numbers)
    return numbers

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5]))
print(rescale_to_unit([0.0, 0.0, 0.0, 0]))
print(rescale_to_unit([1.5, 0.0, 2.0, 1]))
print(rescale_to_unit([1.5, 1.0, 2.0, 1]))
```