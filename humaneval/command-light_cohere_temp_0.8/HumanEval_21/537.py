```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Input numbers are expected to be in ascending order.
    If input: numbers
    assert len(numbers) >= 2
    assert all(n >= 1 for n in numbers)
    result = [0.0] + [numbers * [1.0] / numbers
    dry_lift(numbers, 0.0)]
    return result

def dry_lift(numbers: List[float], start: float):
    """ Given list of numbers, apply a linear transform to that list,
    such that the sum of all elements is equal to start
    Input numbers are expected to be in ascending order
    """ assert len(numbers) >= 1
    assert all(n >= start + 1 for n in numbers)
    result = [start + i for i in numbers]
    return result

numbers = [0.0, 1.0, 2.0, 3.0, 4]

start = 0
print("Sum of elements: ", sum(numbers))
print("Sum of after applying dry lift: ", sum(dry_lift(numbers, start))))
```
This script defines a function called **rescale_to_unit** that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. The function uses the dry_lift approach, which starts with the smallest number and then adds the next number in the list until the sum is equal to the desired start value.