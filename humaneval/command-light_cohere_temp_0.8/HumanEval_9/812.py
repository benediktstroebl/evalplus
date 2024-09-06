```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list of integers.
    Parameters:
    - numbers (List[int]): List of integers
    Returns:  List[int] - List of rolling maximum elements found until the given moment in the sequence
    """
    # Initialize the rolling array with the first element of the input list
    rolling_maxes = [numbers[0]]
    
    # Loop through the input list and add current element to the rolling array
    for num in numbers[1:]:
        rolling_maxes.append(max(rolling_maxes[-1], num))
    
    return rolling_maxes
```