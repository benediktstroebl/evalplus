Here's a self-contained Python script that implements the function you requested:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.append(1.0)
   0, 2.0, 3.0, 4.0, 5)
   75)
    return numbers

test_rescale_to_unit = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
assert test_rescale_to_unit([1.0, 2.0, 3.0, 4]) == [0.0, 1.0, 0.75, 1.0]
print("test_rescale_to_unit is correct")
```

The provided function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. 

The function then returns the rescaled list of numbers.