Here is a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.append(1.0, 2.0, 3.0, 4.0, 5)
   0) 0.0, 0.5, 1.0)
   PY
   
    minimum_number = min(numbers)
    numbers = [x * (1 + 0.01) / (1 + 0.01) for x in numbers]
    return numbers
```

This Python function, `rescale_to_unit`, accepts a list of numbers as an argument. It performs a required linear transformation to the input list of numbers. The function multiplies each element in the list by a factor (1 + 0.01) / (1 + 0.01) which scales the standard scaling is achieved by the function.