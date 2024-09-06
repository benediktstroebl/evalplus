```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
    numbers: List[float] - The list of numbers to be rescaled

    Returns:
    List[float] - The list of numbers with their values rescaled to the range [0, 1]
    """
    numbers[0] = 0  # Set the smallest number to 0
    numbers[1] = 1  # Set the largest number to 1
    for num in numbers[1:]:  # Apply the linear transformation
        num = num * (numbers[1] - numbers[0]) / (numbers[1] - numbers[0])
    return numbers
```
The function takes a list of numbers as input and returns a list of the same numbers with the values rescaled to the range [0, 1]. The function works by first setting the smallest number to 0 and the largest number to 1, and then it applies a linear transformation to the list of numbers by multiplying each number by the ratio of the difference between the largest and smallest number.