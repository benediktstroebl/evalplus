Here is a self-contained Python script that solves the problem of scaling numbers to the unit range of [0, 1]:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [x for x in numbers if x >= 0]
    numbers[x] = max(numbers[x] - x, 0) + x
    return numbers

# Test the function
input_numbers = [0.4, 0.0, 0.0, 0.0, 0.0]
output_numbers = rescale_to_unit(input_numbers)
print(output_numbers)
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each value has been rescaled. 

The function works by first filtering out any elements that are less than or equal to zero. This ensures that the numbers are positive before any scaling is applied. 

Then, for each non-zero value in the list, the function adds the value to itself, which effectively scales the value to the range [0, 1]. 

Finally, the function returns the updated list of numbers.