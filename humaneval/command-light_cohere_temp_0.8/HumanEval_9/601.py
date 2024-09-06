```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    This function takes a list of integers and returns a list of rolling maximum elements found in that sequence. 
    It uses the strategy where it adds a window of 2 and keeps the maximum element from the previous window.
    Args:
        numbers (List[int]): The list of integers.
    Returns: 
    List[int]): A list of rolling maximum elements.
#Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```