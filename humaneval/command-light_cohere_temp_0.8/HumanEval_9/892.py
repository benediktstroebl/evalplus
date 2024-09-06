```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Get the maximum element of the list after applying rolling window 
    technique to it.
    Returns a max element and the list of all elements in decreasing order.
    """
    done using: 
    return [num for num,i in enumerate(numbers) if i>0 and num >= numbers[i-1]]
```