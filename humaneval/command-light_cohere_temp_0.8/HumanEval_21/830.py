```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Input:
        numbers: The input list of float numbers
    
    Output:
        new_numbers: The output list of float numbers, with the applied linear transform
    
    """
    # Initialize a counter for the number of elements in the list
    num_elements = len(numbers)
    
    # Initialize an array to store the rescaled numbers
    new_numbers = [0] * num_elements
    
    # Apply the linear transform to each element of the list
    for i in range(num_elements):
        # Apply the transform
        new_numbers[i] = (numbers[i] / float(max(numbers)))
    
    # Return the new list with the rescaled numbers
    return new_numbers
```