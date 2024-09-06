Here's a Python script that includes a self-contained function `rescale_to_unit`, which solves the problem of scaling numbers between 0 and 1, given a list of floats:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    """
    numbers_sorted = sorted(numbers)
    unit_transformation = numbers_sorted[1:] - numbers_sorted[0]
    transformed_numbers = [x + unit_transformation for x in numbers_sorted]
    return transformed_numbers

# Test the function
input_numbers = [0.2, 0.0, 0.0, 0.5, 0.75]

result = rescale_to_unit(input_numbers)

print(result)
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the numbers in a rescaled unit (between 0 and 1). The function sorts the input list, calculates the unit transformation as the difference between the first and last elements, and then applies this transformation to each element of the input list.