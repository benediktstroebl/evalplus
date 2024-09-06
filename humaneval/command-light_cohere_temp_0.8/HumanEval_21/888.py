```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    - The numbers: List of floating-point numbers
    Returns: A list of numbers, after applying the linear transformation
    """
    # Determine the range of the numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Apply the transformation
    numbers = [num / (max_num - min_num) for num in numbers]
    
    return numbers
``` 
This solution uses the 'rescale_to_unit' function that, given a list of numbers, applies a linear transformation to that list. The function calculates the range of the numbers and applies the transformation based on the difference between the maximum and minimum numbers. The final result is the same as the input, which is the desired behaviour.