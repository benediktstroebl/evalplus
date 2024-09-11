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
    rolling_max_elements = []
    
    # Initialize the maximum element to negative infinity
    max_element = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # Update the maximum element if the current number is greater
        max_element = max(max_element, num)
        
        # Append the current maximum element to the result list
        rolling_max_elements.append(max_element)
    
    return rolling_max_elements


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test cases:
assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert rolling_max([]) == []
```