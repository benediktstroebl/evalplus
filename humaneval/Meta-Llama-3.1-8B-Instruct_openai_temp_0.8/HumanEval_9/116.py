```markdown
### Rolling Maximum Elements

This script generates a list of rolling maximum elements from a given list of integers.
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
    if not numbers:
        return []
    
    result = [numbers[0]]
    for num in numbers[1:]:
        if num >= result[-1]:
            result.append(num)
        else:
            result.append(result[-1])
    
    return result


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple and efficient approach to calculate the rolling maximum elements. It initializes the result list with the first element of the input list, and then iterates over the rest of the list. For each element, it checks if it is greater than or equal to the last element in the result list. If it is, it appends the current element to the result list. Otherwise, it appends the last element in the result list, which is the rolling maximum up to that point.