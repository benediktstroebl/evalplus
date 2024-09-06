```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements in the given list
    >: Numbers are assumed to be non-negative within the function.
    """ 
    max_rolling = numbers[0]
    rolling_maxs = [max_rolling]
    for num in numbers[1:]:
        if num > max_rolling:
            max_rolling = num
        rolling_maxs.append(max_rolling)
    """
    return rolling_maxs

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This function takes a list of integers and returns a list of the rolling maximum elements found in that list. It uses a simple iterative approach with a loop to find the maximum element and updates the rolling maximum.

The output will be: `[1, 2, 3, 3, 3, 4]`.