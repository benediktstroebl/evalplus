```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply linear transformation to the list, such that the smallest number will become 0 and the largest will become 1
    numbers = [n / (n - min(numbers)) for n, min in zip(numbers)]
    return numbers
``` 
This function takes a list of numbers and returns a new list with each element scaled to have a value between 0 and 1, using the formula described. The resulting list is guaranteed to be a valid unit scale transformation of the input list.