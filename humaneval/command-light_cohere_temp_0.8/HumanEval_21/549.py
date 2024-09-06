Here is a self-contained Python script that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers_rescaled = []
    for num in numbers:
        num_rescaled = (num - min(numbers)) / (max(numbers) - min(numbers))
        numbers_rescaled.append(num_rescaled)
    return numbers_resced

In this script, we define the `rescale_to_unit` function that takes a list of numbers as input and returns a new list where each number has been rescaled to be between 0 and 1. We use the goal to calculate the new value by subtracting the smallest number in the list from each original number, and then dividing by the difference between the largest and smallest number in the list.

The resulting list will have each number in the list rescaled to the desired range.