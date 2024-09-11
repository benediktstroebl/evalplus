### Rolling Maximum Function in Python
#### Description

The following Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until that moment in the sequence.

#### Code
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
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_elements = []

    # Initialize the maximum element as negative infinity
    max_element = float('-inf')

    # Iterate over each number in the input list
    for num in numbers:
        # If the current number is greater than the maximum element, update the maximum element
        if num > max_element:
            max_element = num
        
        # Append the maximum element to the list of rolling maximum elements
        rolling_max_elements.append(max_element)

    # Return the list of rolling maximum elements
    return rolling_max_elements

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
#### Explanation

The `rolling_max` function initializes an empty list `rolling_max_elements` to store the rolling maximum elements and sets the initial maximum element to negative infinity.

The function then iterates over each number in the input list. If the current number is greater than the maximum element, it updates the maximum element. The maximum element is then appended to the `rolling_max_elements` list.

Finally, the function returns the `rolling_max_elements` list, which contains the rolling maximum elements found until each moment in the sequence.