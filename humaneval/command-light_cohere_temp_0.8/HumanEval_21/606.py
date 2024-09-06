```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    : 
    #   transform (x) = (x - min(numbers)) / (max(numbers) - min(numbers))
    :     return [transform(num) for num in numbers]
``` 
The function takes a list of numbers and returns a new list with the numbers in the original list but transformed. The transform ensures that the smallest number in the list becomes 0, and the largest number becomes 1.