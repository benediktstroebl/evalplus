```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates and returns the list of rolling maximum elements found in the given list.
    Args:
    numbers (List[int]): The list of integers to generate rolling maximum on.
    Returns: list[int]: A list of rolling maximum elements.
    """
code

    ```
    numbers = [1, 2, 3, 2, 3, 4, 2]
    numbers.max = max(numbers)
    rolling_max = [numbers[i] for i in range(len(numbers))]
    rolling_max.append(numbers[-1])
    return rolling_max
```

This function takes a list of integers as input and returns a list of rolling maximum elements found in the list. It achieves this by calculating the maximum element in the list, generating a list of rolling maximum elements by indexing from the list, and appending the last element to the rolling maximum list.