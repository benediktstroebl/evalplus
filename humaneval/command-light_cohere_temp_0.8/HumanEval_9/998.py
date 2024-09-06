```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generates a list of rolling maximum elements found until the given moment 
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the rolling window maximum list
    rolling_max = [num for num in numbers]

    # Update the rolling window maximum list with the current element
    rolling_max[1::len(rolling_max)] = numbers[0]
    rolling_max = [x for x in rolling_max if x > numbers[i]]
    
    return rolling_max
```