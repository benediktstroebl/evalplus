### Rolling Maximum Element
#### A Python Script to Find Rolling Maximum Elements in a Sequence

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
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last element in the result list,
        # append it to the result list; otherwise, append the last element in the result list
        result.append(max(num, result[-1]))

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we define a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple and efficient approach to compute the rolling maximum elements. It initializes the result list with the first element of the input list and then iterates over the input list starting from the second element. For each element, it checks whether it is greater than the last element in the result list. If it is, it appends the element to the result list; otherwise, it appends the last element in the result list. The function finally returns the result list, which contains the rolling maximum elements.