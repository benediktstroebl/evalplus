```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers[:0] = 0
    numbers = [x / 100.0 for x in numbers] + [100.0] * numbers[1]
   return numbers
```
This function takes a list of numbers as input and returns a new list with the numbers scaled to the unit [0, 1]. The function works by first setting the first element of the input list to 0, then adding 100.0 to each subsequent element to scale it to the unit.