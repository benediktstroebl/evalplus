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
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_element = numbers[0]

    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        rolling_max_list.append(max_element)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines the `rolling_max` function as specified, along with a test case to verify its correctness. The function iterates through the input list, updating the maximum element encountered so far and appending it to the `rolling_max_list`. The function handles edge cases, such as an empty input list, by returning an empty list.