Here's the self-contained Python function that solves the problem:

```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Initialize result list with original numbers
    result = numbers
    
    # Calculate the rescaled numbers
    for num in numbers:
        result.append( (num - 1.0) / (max(numbers) - 1.0)
    
    # Return the copy of the rescaled numbers to the original numbers list
    numbers = result.copy()
    final result list
    return numbers
```

This function, `rescale_to_unit`, takes a list of numbers as input and applies a linear transformation to that list. The transformation ensures that the smallest number becomes 0 and the largest becomes 1. 

The function works by first initializing a result list with the original numbers. Then, it iterates over each number in the input list and computes the rescaled value by multiplying the original number by 1 / (max(numbers) - 1.0). Finally, the result the list with the rescaled numbers, and finally, the function returns the updated list, which now contains the original numbers rescaled to the unit.

This is a self-contained function that does not rely on any external variables or functions, and it can be used directly in other Python scripts or code blocks.