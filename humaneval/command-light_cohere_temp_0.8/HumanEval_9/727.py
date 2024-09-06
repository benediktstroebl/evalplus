```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
    >>> numbers = [10, 20, 30, 40, 50, 60, 70]
    >>> rolling_max(numbers)  # [MAX, MAX, 40, 50, 60, 70]
    """
    numbers = List(set(numbers))  # Remove duplicates
    max_num = numbers[0]
    rolling_max_list = [max_num]
    
    for num in numbers[1:]:
        max_num = max(max_num, num)
        rolling_max_list.append(max_num)
        
    return rolling_max_list
```