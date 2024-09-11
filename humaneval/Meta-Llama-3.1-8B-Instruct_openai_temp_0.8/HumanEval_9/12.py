### Rolling Maximum Problem Solution
Here is a self-contained Python script that solves the rolling maximum problem.

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
    rolling_max_list = []
    current_max = float('-inf')  # Initialize current max as negative infinity

    for num in numbers:
        # If current number is greater than current max, update current max
        if num > current_max:
            current_max = num
        # Append the current max to the result list
        rolling_max_list.append(current_max)

    return rolling_max_list


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max(numbers)
    print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple and efficient approach by iterating through the input list and keeping track of the current maximum element found so far. It achieves this by initializing the `current_max` variable to negative infinity and then updating it whenever a larger number is encountered. The running maximum at each step is appended to the `rolling_max_list` which is returned as the result.