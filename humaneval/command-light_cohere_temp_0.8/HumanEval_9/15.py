```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = numbers[0]
    rolling_max_elements = [max_num]
    for num in numbers[1:]: 
        if num > max_num:
            max_num = num 
        rolling_max_elements.append(max_num)
    rolling_max_elements.
    return rolling_max_elements
```