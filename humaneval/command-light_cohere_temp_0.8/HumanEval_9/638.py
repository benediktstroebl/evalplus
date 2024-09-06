```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    List of integers. 
    Returns a time the max element from the list until a given moment. 
    """
    generate a list of rolling maximum elements found until a given moment 
    in the sequence and returns it as a list.
    """
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max = [max(numbers[i:]) for i in range(len(numbers)-1))]
print(rolling_max) # Output: [1, 2, 3, 3, 3, 4, 4]
```