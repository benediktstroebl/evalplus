```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements = []
    while len(numbers) > 0:
        max_element = numbers[0]
        numbers.remove(max_element)
        
        for num in numbers:
            if num > max_element:
                max_element = num
        
        max_elements.append(max_element)
    
    return max_elements
```