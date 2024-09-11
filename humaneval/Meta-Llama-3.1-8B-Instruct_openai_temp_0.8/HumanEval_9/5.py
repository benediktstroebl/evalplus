### Rolling Maximum Problem Solution
#### Problem Statement
From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution

```markdown
### rolling_max.py
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store rolling max elements
    rolling_max_elements = []

    # Initialize the rolling max with the first element of the input list
    current_max = numbers[0]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Update the rolling max if the current number is greater
        if num > current_max:
            current_max = num
        # Append the rolling max to the result list
        rolling_max_elements.append(current_max)

    return rolling_max_elements


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this solution, we use a simple iteration approach. We maintain a `current_max` variable to track the rolling maximum element. We iterate over the input list, and for each number, we update `current_max` if the current number is greater. Finally, we append `current_max` to the result list. This solution has a time complexity of O(n), where n is the length of the input list.