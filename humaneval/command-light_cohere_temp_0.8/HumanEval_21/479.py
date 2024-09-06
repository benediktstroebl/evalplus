```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n+1) for n in numbers]
    return numbers
``` 
This function computes a linear transformation for the input list of numbers, such that the smallest number becomes 0 and the largest becomes 1, ensuring that the original range of numbers is preserved.

The function takes a list of numbers as input and returns a new list with the same elements but in a scaled-down range. 
This approach is suitable for preparing data for visualization in many machine learning tasks, especially when the range of input data is critical.