```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum elements.
    """
    if not numbers:
        return []

    max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_values.append(current_max)

    return max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test with an empty list:
empty_list = []
print(rolling_max(empty_list))  # Output: []

# Test with a list containing a single element:
single_element_list = [5]
print(rolling_max(single_element_list))  # Output: [5]
```