```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.
    """
    if not numbers:
        return []

    rolling_max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        current_max = max(current_max, num)
        rolling_max_values.append(current_max)

    return rolling_max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```