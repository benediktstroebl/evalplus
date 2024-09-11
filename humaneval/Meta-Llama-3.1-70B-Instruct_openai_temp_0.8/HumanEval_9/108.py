```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.
    """
    if not numbers:
        return []

    max_until_now = numbers[0]
    result = [max_until_now]
    
    for num in numbers[1:]:
        max_until_now = max(max_until_now, num)
        result.append(max_until_now)
    
    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test cases:
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
print(rolling_max([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
```