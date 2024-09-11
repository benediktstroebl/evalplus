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
    if not numbers:  # Check if the input list is empty
        return []

    max_so_far = numbers[0]  # Initialize the maximum found so far with the first element
    result = [max_so_far]  # Initialize the result list with the first maximum

    for num in numbers[1:]:  # Iterate over the rest of the list
        if num >= max_so_far:  # If the current number is greater than or equal to the maximum found so far
            max_so_far = num  # Update the maximum found so far
        result.append(max_so_far)  # Append the maximum found so far to the result list

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```