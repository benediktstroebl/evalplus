```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n for n in numbers if n >= 0]
    numbers[::2] = numbers[::2] / (numbers[0] - numbers[1])
    return numbers
```
The function applies a linear transformation to the numbers in the list so that the smallest number becomes 0 and the largest becomes 1. 

The function uses the expression numbers[::2] to select every second element in the list numbers. 
The expression numbers[::2] / (numbers[0] - numbers[1]) is used to calculate the linear transformation. 
The function then returns the list with the transformation applied to each element. 
This function can be used to convert a list of numbers into a unit of 0-1.