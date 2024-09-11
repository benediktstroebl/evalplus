### Rolling Maximum Element Finder
#### Python Script

```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    max_elements = []

    # Initialize the maximum element as negative infinity
    max_so_far = float('-inf')

    # Iterate over the input list
    for num in numbers:
        # Update the maximum element if the current number is larger
        if num > max_so_far:
            max_so_far = num
        
        # Append the maximum element to the result list
        max_elements.append(max_so_far)

    # Return the list of rolling maximum elements
    return max_elements

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script uses a simple iterative approach to find the rolling maximum element in a list of integers. It maintains a running maximum element `max_so_far` and updates it whenever a larger number is encountered. The script then appends this maximum element to the result list, ensuring that the list contains the maximum element found up to each point in the sequence.