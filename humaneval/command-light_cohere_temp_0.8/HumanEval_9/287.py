```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    Input: numbers - List[int]
    Output: List[int]
    """
    # Initialize the rolling window max
    rolling_max_values = [num for num in numbers]
    current = numbers[0]
    
    # Loop through the sequence to find the rolling maximum
    for num in numbers[1:]:
        # Update the current value with the new element
        current = max(num, current)
        
        # Save the current maximum value as the next element in the list
        rolling_max_values.append(current)
    
    return rolling_max_values
```