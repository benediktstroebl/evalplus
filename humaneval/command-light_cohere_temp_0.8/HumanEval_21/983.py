```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input:
    numbers: list[float]  # input list of numbers

    Output:
    rescaled_numbers: list[float]  # output list of rescaled numbers

    """
    # apply the rescaling function to each number in the input list
    rescaled_numbers = [x / 100.0 for x in numbers]  # use list comprehension to apply the rescaling function to each number

    assert all(rescaled_numbers >= 0)  # check the output is non-negative
    assert all(rescaled_numbers <= 1)  # check the output is non-positive
    assert len(set(rescaled_numbers)) == len(rescaled_numbers)  # check the output is sorted
    assert sum(rescaled_numbers) == 1  # check the output is correct

    # test the function with some sample inputs
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    # print the function's output
    print(rescale_to_unit(numbers))
```