### Rolling Maximum Elements in a List
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list of rolling maximum elements.
    
    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    current_max = float('-inf')
    
    for num in numbers:
        # Update current_max if the current number is larger
        if num > current_max:
            current_max = num
        result.append(current_max)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines the `rolling_max` function, which generates a list of rolling maximum elements from the input list `numbers`. It iterates through the list, keeping track of the maximum value encountered so far (`current_max`). If a larger number is found, it updates `current_max`. The rolling maximum for each position is then appended to the `result` list. Finally, the function returns the `result` list, which contains the rolling maximum elements.