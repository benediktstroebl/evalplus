```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers]
    new_numbers = [x * 100.0 for x in numbers]
    return numbers
```

This function accepts a list of numbers as an argument and outputs a new list of numbers with the smallest value set to 0 and the largest value set to 1. This is a approach is based on the definition of the rescale_to_unit function from the previous prompt response.