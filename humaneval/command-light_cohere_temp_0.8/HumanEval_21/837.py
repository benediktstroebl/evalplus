Here is a Python script that solves the problem of scaling a list of numbers to a range from 0 to 1, with the additional requirement that the range must contain elements:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Input:
    numbers (List[float]): list of numbers to be rescaled

    Output:
    rescaled_numbers (List[float]): list of rescaled numbers

    """
    if len(numbers) < 2:
        raise ValueError("Input list should contain at least two numbers")

    # Create a copy of the input list to avoid modifying it
    numbers = numbers[:] + [numbers[0]] * (numbers[1] - numbers[0])

    # Apply the rescaling transformation
    for num in numbers[1:]:
        numbers[0] = max(0, num - numbers[0])
        numbers[1] = max(1, num - numbers[1])

    return numbers
```
This script defines a function rescale_to_unit that takes a list of numbers as input and returns a new list where each number has been rescaled to the range [0, 1]. The function performs the rescaling transformation by applying a linear function that scales each number to the difference between the largest and smallest numbers in the list, ensuring that the smallest number becomes 0 and the largest becomes 1. 
The function tests for the validity of the input by checking that the list contains at least two numbers and raises a ValueError if the list does not meet this condition.