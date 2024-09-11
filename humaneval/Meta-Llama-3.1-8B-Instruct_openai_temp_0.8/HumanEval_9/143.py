### Rolling Maximum Element

Here's a Python script that uses a simple iterative approach to find the rolling maximum element in a given list of numbers.

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
    result = []
    max_so_far = float('-inf')  # Initialize max_so_far with negative infinity
    
    for num in numbers:
        if num >= max_so_far:  # If current number is greater than or equal to max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize `max_so_far` with negative infinity to ensure that the first number in the list is always considered the maximum. Then, for each number in the list, we check if it's greater than or equal to `max_so_far`. If it is, we update `max_so_far` with the current number. Finally, we append `max_so_far` to the result list. This way, we effectively keep track of the rolling maximum element at each position in the list.