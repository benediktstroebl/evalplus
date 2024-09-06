```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers. 
    Input: numbers List[1,2,3,2,4]
    Output: [1,3,4]
    """
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)
```