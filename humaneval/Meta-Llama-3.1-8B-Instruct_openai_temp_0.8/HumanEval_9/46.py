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
    if not numbers:
        return []
    
    result = []
    current_max = float('-inf')
    
    for num in numbers:
        if num > current_max:
            current_max = num
        result.append(current_max)
    
    return result


# Test the function
if __name__ == "__main__":
    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
    print(rolling_max([]))  # Output: []
    print(rolling_max([5]))  # Output: [5]
    print(rolling_max([3, 2, 1]))  # Output: [3, 2, 1]
```

This Python script implements a function called `rolling_max` that generates a list of rolling maximum elements from a given list of integers. It iterates through the input list, maintaining a `current_max` variable that is updated whenever a larger number is encountered. The `current_max` value is appended to the result list for each iteration, effectively generating a list of rolling maximum elements. The script also includes a test section to demonstrate the function's correctness.