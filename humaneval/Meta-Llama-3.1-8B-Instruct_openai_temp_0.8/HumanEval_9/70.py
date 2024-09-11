### Rolling Maximum Elements
#### Problem Statement

From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
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
    result = [numbers[0]]  # Initialize result list with the first element
    for i in range(1, len(numbers)):
        # Update result list with the maximum of the current element and the last element in the result list
        result.append(max(numbers[i], result[-1]))
    return result


# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes the result list with the first element of the input list and then iterates over the rest of the list, updating the result list with the maximum of the current element and the last element in the result list. The function returns the result list. The example usage demonstrates how to use the function to find the rolling maximum elements in a given list.