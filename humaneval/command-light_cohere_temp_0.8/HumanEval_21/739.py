```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # transform the list such that the smallest number becomes 0 and the largest becomes 1
    numbers[0] = 0
    numbers = [x + y for x, y in zip([0.0] + numbers)]
    smallest = min(numbers)
    for x in numbers:
        x = max(0.0, x - 1.0)
   0
   0, numbers[x] = x
    return numbers

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
# [0.0, 0.5, 0.0]
print(rescale_to_unit([0.0, 2.0, 3.0, 4.0, 5]))
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0]))
print(rescale_to_unit([1.5, 2.0, 3.0, 4]))
```