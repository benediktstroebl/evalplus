```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x * 0.5 for x in numbers] + [x * 0.1 for x in numbers]
    return numbers
```
This Python code defines a function called `rescale_to_unit` that takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number in the original list will become 0 and the largest number will become 1. The function achieves this by creating a new list where each element in the input list is multiplied by a factor of 0.5 and then with the original element and multiplied by a factor of 0.5, respectively. This is creates the for the result of the transformation, the function then returns the new list.