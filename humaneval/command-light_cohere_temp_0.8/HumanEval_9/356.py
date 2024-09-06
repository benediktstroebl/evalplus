```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found in the given list
    """
    numbers.append(numbers[0]) 
    rolling_max_elements = [max(numbers[:i]) for i in range(1, len(numbers))]
    return rolling_max_elements

# Test case
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_elements = rolling_max(numbers)
print("Rolling Maximum elements:",rolling_max_elements) # [1, 2, 3, 3, 3, 4, 4]
```