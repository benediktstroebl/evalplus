### Rolling Maximum
#### Problem Description

From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.
    """
    # Initialize an empty list to store the rolling maxima
    rolling_maxima = []
    
    # Initialize the current maximum to negative infinity
    current_max = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # If the current number is greater than the current maximum, update the current maximum
        if num > current_max:
            current_max = num
        
        # Append the current maximum to the rolling maxima list
        rolling_maxima.append(current_max)
    
    # Return the list of rolling maxima
    return rolling_maxima

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this solution, we initialize an empty list `rolling_maxima` to store the rolling maxima and a variable `current_max` to keep track of the current maximum. We iterate over each number in the input list, updating `current_max` if we find a larger number. We append `current_max` to `rolling_maxima` at each iteration, resulting in a list of rolling maxima.