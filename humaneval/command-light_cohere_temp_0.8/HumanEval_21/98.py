```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (1 + n) for n in numbers]
    return numbers
```
This Python code defines a function called rescale_to_unit that takes a list of numbers as input and returns a new list with each element scaled to be between 0 and 1.

The function uses a formula to calculate the rescaled values, which involves dividing each number in the input list by the sum of the input list plus one.

The formula ensures that the smallest number becomes 0 and the largest number becomes 1 after the rescaling process. 
The function then returns the new list with the rescaled values.