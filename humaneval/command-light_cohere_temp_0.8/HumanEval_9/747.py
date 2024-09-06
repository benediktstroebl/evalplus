```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element in the generation is the maximum value of the rolling window
    until the next element.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the list of rolling window maximum values
    rolling_max_values = [num for num in numbers]
    
    # Iterate through the elements of the numbers list
    for i, current_num in enumerate(numbers):
        # Calculate the rolling window maximum for the current number
        rolling_window_max = current_num
        
        # Update the rolling_max_values list with the current maximum value
        rolling_max_values[i+1] = current_num
        rolling_max_values[i] = rolling_window_max
        
        # Return the final list of rolling maximum values
        return rolling_max_values
```
This script defines a rolling_max function that generates a list of rolling maximum elements from a given list of integers. It uses a approach where the `rolling_max_values` list, which is initialized with the numbers from the input list. The loop iterates through each element in the numbers list, and the current maximum value of the rolling window is calculated. The `rolling_max_values` list is then updated with the current maximum value and the previous maximum value. The loop continues until the maximum value converges to the current element, and the `rolling_max_values` list reflects the rolling window maximum values at each index.