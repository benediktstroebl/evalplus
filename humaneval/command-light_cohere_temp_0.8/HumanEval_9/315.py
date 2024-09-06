```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found in the given sequence """
    # Initialize the rolling max list
    rolling_max = [num for num in numbers]
    
    # Add current element to the rolling max list
    rolling_max.append(numbers.append(numbers[-1])  # Retain the oldest element as it is the max so far
    # Initialize max variable
    max = numbers[0]
    
    # Loop through the sequence
    for num in numbers[1:]:
        # Compare current number with the max so far
        if num > max:
            max = num
        # Save the current max number
        rolling_max.append(max)
        rolling_max.append(max)
    
    return rolling_max
``` 
Do you require any other assistance with this?