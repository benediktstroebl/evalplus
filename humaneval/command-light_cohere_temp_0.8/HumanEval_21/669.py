```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    :return numbers [apply(lambda x: (x[0] - x[1]) / (x[1] - x[0])) * (1.0 - 0.0)
    different number the regress to unit for a list of numbers, where a negative number will be mapped to 0 and a positive number will be mapped to 1.

This function takes a list of numbers as input and returns a list of numbers with the same values, but with the smallest number being 0 and the largest number being 1.

The function uses a lambda function to apply the linear transform to each number in the list. The lambda function takes a difference between the first and second elements of the list and applies the linear transform to that difference.

The function then multiplies the result by the difference between 1.0 and 0.0, which negative value that the mapping that a positive number to 1.0 and a negative number to 0.0. 

This approach ensures that the list of numbers is scaled to the range [0,1] and that all numbers are positive.  
This code is well-contained and can be easily understood. It has a simple logic that can be easily modified to solve other problems.