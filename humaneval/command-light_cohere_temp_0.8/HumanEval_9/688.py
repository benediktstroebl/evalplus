```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from the given list of integers.
    Args: 
        numbers (List[int]): A list of integers
    Returns: 
        List[int]: A list of rolling max elements found until the given moment in the sequence.
    """
    example: 
    numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = list(set(numbers))  # remove duplicates
    res = [x for x in numbers if numbers.count(x(x)=1]
    return res
```