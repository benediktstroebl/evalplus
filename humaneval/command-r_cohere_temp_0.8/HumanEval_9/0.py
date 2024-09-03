```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of the rolling maximum element found 
    until that moment in the sequence.
    
    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list containing the rolling maximum values
    """
    if not numbers:
        return []

    rolling_max_values = [numbers[0]]
    max_val = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
            rolling_max_values.append(max_val)
        else:
            rolling_max_values.append(rolling_max_values[-1])

    return rolling_max_values
```