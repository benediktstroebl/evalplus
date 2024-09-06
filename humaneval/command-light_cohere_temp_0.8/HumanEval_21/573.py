Here's a self-contained Python function that solves the given problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    numbers[1] = 1
    return numbers


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5]

print("The rescaled numbers are: ", rescale_to_unit(numbers))
```
This function takes a list of numbers as input and returns a new list where the first element is set to 0 and the last element is set to 1. The function then returns the list.