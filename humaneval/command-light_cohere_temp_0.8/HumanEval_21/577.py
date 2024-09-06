```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n + 1) for n in numbers]
    return numbers
```
This function allows you to convert a list of numbers to a unit scale, where the smallest number is 0 and the largest number is 1.  It is test this list of numbers against a given linear function that scales numbers upwards.