Here's the solution to the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: [float] input list
    :return: [float] modified list
    numbers.res rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
    first number will become 0 and the last will become 1
    """
    numbers = [x for x in numbers if x < 0]
    numbers.append(1)
    numbers.extend([x0]*len(numbers)
    return numbers
```