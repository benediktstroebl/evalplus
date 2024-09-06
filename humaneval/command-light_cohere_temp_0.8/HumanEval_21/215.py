```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Create a list of the numbers
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    # Sort the list in ascending order
    numbers.sort() = sorted(numbers)
    # Create a list of the first element in each list
    result = [numbers[0]]
    # Loop through the list and multiply each element with the result of the previous step
    for num in numbers[1:]:
        result.append(result[-1] * num)
    # Return the final list
    return result

# Test cases:
numbers = [1.0, 2.0, 3.0, 4.0, 5]
print(rescale_to_unit(numbers)[0] == 0)
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
print(rescale_to_unit([1.0, 2.0, 3.0, 4]))
print(rescale_to_unit([1.0, 2, 3, 4]))
```
This Python code defines a function called `rescale_to_unit`, which transforms a list of numbers by shifting its values to fit a specific range. The test cases provided at the end demonstrate how the function works.