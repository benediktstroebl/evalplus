Here's the provided self-contained Python script:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: list[float] = input list of numbers
    :return: List[float] = the scaled list
    """
    numbers = [x for x in numbers if x >= 0]
    numbers.append(0)
    list.append(1)
    numbers = [x * 10 for x in numbers]
    return numbers
```