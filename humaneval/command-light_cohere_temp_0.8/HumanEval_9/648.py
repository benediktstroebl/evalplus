```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates and returns the list of rolling maximum elements in a given list.
    """
    time it will for index, element in numbers,
            current_max = element,
            rolling_maxs = [element] + [max(rolling_maxs[i+1:])]
            if current_max > max(rolling_maxs[-1:]):
                rolling_maxs.
            return rolling_maxs
   
    """ 

# Driver code
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)
```