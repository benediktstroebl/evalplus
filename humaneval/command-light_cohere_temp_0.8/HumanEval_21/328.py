```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters: numbers: List[float]
    Returns: List[float]
    """
    # make sure we have at least 2 elements in numbers
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")

    # find the range of numbers and set smallest to 0 and largest to 1
    min_num = min(numbers)
    max_num = max(numbers)
    numbers = [x - min_num for x in numbers] + [max_num] + [max_num - min_num]
    return numbers

# test the function
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.5]
return rescale_to_unit(numbers)
```