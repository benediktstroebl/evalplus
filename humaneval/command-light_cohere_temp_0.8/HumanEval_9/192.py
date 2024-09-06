```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, index in sorted((num, index) for index, num in enumerate(numbers)) 
                if num > numbers[index + 1]]
```