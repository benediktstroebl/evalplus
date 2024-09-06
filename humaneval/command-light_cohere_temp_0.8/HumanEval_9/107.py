```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of rolling maximum elements found until a given moment 
    in the sequence.
    Returns a format: [max_1, max_2, ..., max_n]
    """
    numbers = sorted(numbers)
    max_index = numbers.find_index(max(numbers))
    return [x for x in numbers[:max_index]] + [x for x in numbers[max_index+1:]]
``` 
This script defines a function `rolling_max` that takes a list of integers and returns a list of the maximum elements, considering the list's order. The code is self-contained and efficient, using the `find_index` function to find the index of the maximum element and then using slicing to get the rolling maximum elements.