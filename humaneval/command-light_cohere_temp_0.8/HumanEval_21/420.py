```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    : 
    numbers = [n//100.0 for n in numbers] + [100.0] * [n//n//100.0]
    if n < 0.0 and n> float > 1.0
   0 else
    Hewit h-> if not list_can_be_list(numbers) else
    raise TypeError("Input must be a list")
    return numbers
```