```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a given list of integers.
    Return a list with the maximum element as the first element and the rest as the rolling 
    maximum sequence until the next moment.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 2:
        return [numbers[0]]
    
    rolling_maxes = [numbers[0]]
    for num in numbers[1:]:
        current = num
        for i in range(len(rolling_maxes) - 1, -1, -1):
            if rolling_maxes[i] > current:
                rolling_maxes[i] = current
        current = num
    
    return rolling_maxes
```  The function takes a list of integers as input and returns a list of integers that contains the maximum element found in the list, and each following element in the list will be the rolling maximum until the next moment. 
function is self-contained, and it does not require any external functions or classes to be called.