```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found in the given list.
    """
    List comprehension is a good way to do it?
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [max(numbers[i:i+1]) for i in range(len(numbers)-1)]
``` 
The function uses a list comprehension to calculate the rolling maximum elements in the numbers list.