```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns a list of the maximum element found while moving the window (considering all the elements in numbers[0:i]) over.
    It uses list comprehensions to find the maximum.
    """
   
        list comprehension is like:
    numbers[0:i] == [numbers[j] for j in range(i+1, len(numbers))] 
    for i in range(len(numbers)-1))
    """
    return [numbers[j] for j in range(i, len(numbers))]
```