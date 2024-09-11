```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment 
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.
    """
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Update the result list with the maximum of the current number and the last element of the result list
        result.append(max(num, result[-1]))
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which calculates the rolling maximum of a given list of integers. It initializes the result list with the first element of the input list and then iterates over the input list starting from the second element, updating the result list with the maximum of the current number and the last element of the result list. The function returns this result list. The example usage demonstrates how to call this function with a sample list of numbers and print the result.