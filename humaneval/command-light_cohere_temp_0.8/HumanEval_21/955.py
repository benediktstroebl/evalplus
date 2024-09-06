Here's a Python script that includes a self-contained function to solve the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    if len(numbers)==2:
        numbers[0] = 0
        numbers[1] = 1
        return numbers

    else:
        for x in numbers:
            numbers[0] = 0
            numbers[1] = 1
            x = x * 0.033333333333 / 2
           
            if x<numbers[0]:
                numbers[0] = x
                numbers[1] = 1
            else:
                numbers[0] = 1
                numbers[1] = x

test_list = [1.0, 2.0, 3.0, 4.0, 5]

rescale_to_unit(test_list)
```
The function returns the list after applying the transformation to it.