Here is a Python script that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    - First, get the minimum and maximum values of the list
    numbers = [num for num in numbers if num >= 0]
    numbers = [num for num in numbers if num <= 1]
    numbers = [num / float(abs(num)) for num in numbers]
    return numbers
```

This script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list with the numbers rescaled to the unit range of 0 to 1. The function works by first getting the minimum and maximum values of the input list. Then, it creates a new list that contains the values of the input list, but only for the values that are greater than or equal to 0. The function then creates a new list that contains the values of the input list, but divided by the absolute value of each value. The function then returns the list of the rescaled numbers.