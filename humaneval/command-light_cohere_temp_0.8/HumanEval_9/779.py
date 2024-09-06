```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements from the input list
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4]
    """
    numbers = [num for num in numbers if num != 0] 
    return [max(numbers[i:i+1]) for i in range(len(numbers)-1)]
```