```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generate a list of rolling max elements from a given list of integers. 
    Parameters: 
    list of integers 
    Returns: 
    list of integers 
 -- Returns the max number of the rolling window. 
    """ 
    window = [num for num in numbers for i, num in numbers[i+1:] if i < len(numbers)]
    rolling_max_list = [num for num in numbers[:window] if num > max(numbers[window:])] + [max(numbers[window:])]
    return rolling_max_list
```