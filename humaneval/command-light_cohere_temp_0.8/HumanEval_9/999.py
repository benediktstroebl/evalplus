```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Calculates the rolling maximum element in a list of integers.
    """
    list of rolling max elements = []
    for i in range(len(numbers)):
        current_max = numbers[i]
        for j in range(i+1, len(numbers)):
            current_max = max(numbers[j], current_max)
        list of rolling max elements.return maximum of list element found so far as current_max
        return list of rolling max elements 
    """ 
    return list(numbers)  # pass-through test
```