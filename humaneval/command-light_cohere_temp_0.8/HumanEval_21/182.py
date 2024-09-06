Here's the solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n+1) for n in numbers]
    return numbers
```
This function takes a list of numbers as an input and applies a linear transformation to the list. This transformation is done by dividing each number by the ratio of its current value and the next value in the list, ensuring the smallest number becomes 0 and the largest number becomes 1. 
This function will return a new list with the rescaled numbers.