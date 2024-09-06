```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers. 
    Input:
        numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    return [i for i in set(numbers) if numbers.count(i) > 1]
```