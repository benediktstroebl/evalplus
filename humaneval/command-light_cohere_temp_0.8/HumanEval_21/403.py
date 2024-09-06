Here is a Python script that defines a function `rescale_to_unit` that solves the problem you provided:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (1 + n)) for n in numbers]
    return [i if i < 0 else i + 1 for i in numbers]
```
This function takes a list of numbers as input and returns a new list where each number has been scaled to be between 0 and 1. 

The function works by creating a new list of numbers by dividing each number in the input list by the sum of all the numbers in the input list. This will effectively scale each number to be between 0 and 1, since division by 1 will scale a number to 1.