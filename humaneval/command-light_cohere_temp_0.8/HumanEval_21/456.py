```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: List[float]
    :return: List[float]
    numbers = [x / 100.0 for x in numbers]
    print(numbers)
```
This function takes a list of numbers as input and returns a new list with the same elements, but each number has been divided by 100.

The function then prints out the input list, which should be the output list with the numbers divided by 100.

This self-contained Python script demonstrates the core functionality of the rescale_to_unit function, passing it as an example use case.