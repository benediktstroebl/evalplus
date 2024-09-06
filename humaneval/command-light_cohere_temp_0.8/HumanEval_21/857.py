```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers[0] = 0
    numbers[1] = 1
    return numbers
```

This Python script defines a function called rescale_to_unit, which takes a list of numbers as input and applies a linear transformation to that list. The function first sets the0 number in the list to 0 and then sets the second number to 1, effectively scaling the numbers in the list between 0 and 1.