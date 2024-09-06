```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [x for x in numbers if x >= 0]
    numbers[0] = 0  # Add first element to the list (putting it to 0)
    numbers[1] = 1  # Add second element to the list (puting it to 1)
    return numbers

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)
print(numbers)  # Output: [0.0, 2.0, 3.0, 5.0]

```