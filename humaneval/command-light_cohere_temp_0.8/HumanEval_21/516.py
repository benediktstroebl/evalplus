Here's the self-contained Python function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers.extend(0.0)
    original list
   0.0, 0.0, 3.0, 4.0, 5)

   
    numbers, return the rescaled list

    """
Test cases:
    ```python
    numbers = [1.0, 2.0, 3.0, 4.0, 5]

    print("The original numbers:", numbers)
    print("The rescaled numbers:", rescale_to_unit(numbers))
    ```