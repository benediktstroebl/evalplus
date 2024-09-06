```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in the sequence.
    Each element in the time sequence is compared to all previous ones, 
    and the maximum is kept track of and returned with the new element.
    >>> test_rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_element = numbers[0]
    rolling_max_list = [max_element] + numbers
    
    for num in numbers[1:]:
        current = num
        # Compare with all previous elements
        for item in rolling_max_list[-2:]:
            if current > item:
                current = item
        rolling_max_list.append(current)
    
    return rolling_max_list
```