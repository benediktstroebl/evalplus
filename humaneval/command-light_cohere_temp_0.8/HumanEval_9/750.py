```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    This function takes a list of integers and returns a list of the 
    rolling maximum elements found in the sequence until a given moment.
    Return list of increasing numbers with the rolling maximum elements. 
    Input: numbers = [1, 2, 3, 2, 3, 4, 2]
    Output: [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.append(max(numbers[:-1]))
    return numbers
```