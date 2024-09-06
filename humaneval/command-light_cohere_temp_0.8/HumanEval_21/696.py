```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [num / (num + 1) for num in numbers]
    return numbers
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been rescaled to be between 0 and 1.  The function utilizes the recursive division by adding 1 to each number in the list, which is the definition of a linear transformation that scales each number to be between 0 and 1.