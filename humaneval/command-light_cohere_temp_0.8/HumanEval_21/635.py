```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Initialize variables
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Apply the transformation
    transformed_numbers = [num / (max_val - min_val)] * (max_val + min_val)
    
    return transformed_numbers
```
This function "rescale_to_unit" takes a list of numbers as input and returns a list of the same numbers after applying a linear transformation to them.