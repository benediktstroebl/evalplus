```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns the list of the rolling maximum element found until the given moment in the sequence.
    Each element in the max sequence is compared to the current maximum element, and the maximum of the current
    sequence is updated accordingly.
    """
    list of rolling maximum elements: [1, 2, 3, 3, 3, 4, 4] 
    """
    numbers = sorted(numbers)  # Sort the input list to have a stable sequence
    max_element = numbers[0]  # Initialize the current maximum element with the first element of the list
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return [max_element]  # Return the list containing the current maximum element
```