```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Input: 
    numbers (List[float]): List of numbers to be transformed
   
    Output: 
    rescaled_numbers (List[float]): Transformed list of numbers, with smallest value becoming 0 and largest value becoming 1
    """
    # Swap smallest and largest elements
    numbers.sort(reverse=True)
    # Initialize result list with smallest number
    rescaled_numbers = [0.0]
   0,
    # Add largest element
    rescaled_numbers.append(numbers[-1])
    # Add all remaining elements in ascending order
    for num in numbers[1:-1]:
        rescaled_numbers.append(num / numbers[-1])
    return rescaled_numbers
```
This function will take a list of numbers and rearrange it such that the smallest number is at index 0 and the largest number is at the end. It will then the final list with the numbers in ascending order.