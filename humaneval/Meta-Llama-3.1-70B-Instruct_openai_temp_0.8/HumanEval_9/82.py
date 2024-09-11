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
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_list = []

    # Initialize the maximum element as negative infinity
    max_element = float('-inf')

    # Iterate over the list of numbers
    for num in numbers:
        # Update the maximum element if the current number is greater
        max_element = max(max_element, num)
        
        # Append the current maximum element to the list
        rolling_max_list.append(max_element)

    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```