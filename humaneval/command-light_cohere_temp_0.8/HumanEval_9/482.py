```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return the list of rolling maximum elements in the given sequence.
    """
    Generate a rolling array (maxed elements in each position, starting from left).
    """
    # Initialize rolling array
    rolling_maxes = [num for num in numbers]
    
    # Add current element to rolling array
    rolling_maxes.append(numbers[0])
    
    # Repeat until reaching end of sequence
    while numbers != []:
        # Find maximum in rolling array
        max_num = rolling_maxes[-1]
        
        # Replace max with the next element in the sequence
        rolling_maxes[0] = numbers[0]
        rolling_maxes[1:] = [numbers[1]]
        numbers[0] = max_num
        
        # Move the rest of the rolling array one element to the right
        rolling_maxes[1::] = rolling_maxes[::]
        
    return rolling_maxes
```
Do you need anything else?