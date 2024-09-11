Here's the Python function that solves the problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers representing the rolling maximum element found until given moment in the sequence.
    """
    if not numbers:
        return []

    rolling_max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_max_values.append(current_max)

    return rolling_max_values

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This function works by initializing the `rolling_max_values` list with the first number in the input list, and setting the `current_max` to the same value. It then iterates over the rest of the numbers in the input list. For each number, it checks if the number is greater than the `current_max`. If it is, it updates the `current_max` to the new number. It then appends the `current_max` to the `rolling_max_values` list. The function finally returns the `rolling_max_values` list.

Note that this function has a time complexity of O(n), where n is the length of the input list, making it efficient for large inputs.