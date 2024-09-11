```markdown
### Rolling Maximum Problem Solution
#### Problem Description
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

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    max_elements = [numbers[0]]
    
    # Iterate over the list of numbers starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last rolling maximum, update the rolling maximum
        if num > max_elements[-1]:
            max_elements.append(num)
        # Otherwise, keep the last rolling maximum
        else:
            max_elements.append(max_elements[-1])
    
    return max_elements

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This solution uses a simple iterative approach to build the `max_elements` list by maintaining the rolling maximum at each position. If the current number is greater than the last rolling maximum, it updates the rolling maximum; otherwise, it keeps the last rolling maximum. The time complexity is O(n), where n is the length of the input list, making this solution efficient for large lists.