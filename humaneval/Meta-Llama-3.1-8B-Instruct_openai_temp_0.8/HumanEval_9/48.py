```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.
    """
    rolling_max_list = []  # Initialize an empty list to store the rolling maximums
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity

    for num in numbers:  # Iterate over the list of numbers
        if num >= max_so_far:  # If the current number is greater than or equal to max_so_far
            rolling_max_list.append(num)  # Add the current number to the rolling maximum list
            max_so_far = num  # Update max_so_far
        else:
            rolling_max_list.append(max_so_far)  # If not, append max_so_far to the rolling maximum list

    return rolling_max_list  # Return the rolling maximum list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script will create a list of rolling maximum elements from the input list of integers. It iterates over the list, comparing each number to the current maximum found (`max_so_far`). If the current number is greater, it updates `max_so_far` and adds the current number to the rolling maximum list. If not, it adds `max_so_far` to the list. This way, the script retains the maximum element found at each step in the sequence.