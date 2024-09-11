### Rolling Maximum Problem Solution
#### Description
This Python script defines a function `rolling_max` that generates a list of rolling maximum elements found until a given moment in the input sequence.

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

    # Initialize the maximum element as the first element in the list
    max_element = numbers[0]

    # Iterate over the list of numbers
    for num in numbers:
        # If the current number is greater than the maximum element, update the maximum element
        if num > max_element:
            max_element = num
        # Append the maximum element to the list of rolling maximum elements
        rolling_max_elements.append(max_element)

    # Return the list of rolling maximum elements
    return rolling_max_elements

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation
The `rolling_max` function initializes an empty list to store the rolling maximum elements and sets the maximum element as the first element in the input list. It then iterates over the list of numbers, updating the maximum element if a larger number is found, and appending the maximum element to the list of rolling maximum elements. Finally, it returns the list of rolling maximum elements.