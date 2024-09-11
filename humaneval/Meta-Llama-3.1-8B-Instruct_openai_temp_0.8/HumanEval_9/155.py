### Rolling Maximum Element

#### Problem Description

From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Generate a list of rolling maximum element found until given moment in the sequence.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    List[int]: A list of rolling maximum elements.
    
    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    max_so_far = numbers[0]
    rolling_max_elements = [max_so_far]
    
    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_elements.append(max_so_far)
    
    return rolling_max_elements

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this solution, we iterate over the input list and keep track of the maximum element seen so far. We also append this maximum element to our result list after each iteration. This way, we get the rolling maximum element for each position in the input list. If the input list is empty, we return an empty list.