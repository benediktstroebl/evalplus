```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return the list of rolling maximum elements found in numbers.
    """
    list of rolling max = []
    for num in numbers: 
        if len(rolling_max) == 0 or num > rolling_max[-1]:
            rolling_max.append(num)
        else:
            rolling_max.append(rolling_max[-1])
        rolling_max.append(num)    
    return rolling_max
```
Do you need anything else?