```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [num for num in numbers if num != 0]  # Remove zeros to avoid infinity
    max_num = numbers[0]
    rolling_max_elements = [max_num]
    
    for num in numbers[1:]:
        current_max = max(max_num, num)
        rolling_max_elements.append(current_max)
        max_num = current_max
    
    return rolling_max_elements
```