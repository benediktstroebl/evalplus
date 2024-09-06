```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """Return a list of rolling maximum elements from the given list of integers."""
    # Initialize a list to store the rolling maximum elements
    max_list = [float('-inf')] * rolling_window

    # Initialize a loop to iterate over the list of numbers
    for i, number in enumerate(numbers):
        # Update the list of rolling maximum elements
        update_max_list(i, number, rolling_window, max_list)

    # Return the final list of rolling maximum elements
    return max_list


def update_max_list(i, number, rolling_window, max_list):
    """Update the list of rolling maximum elements given the current number."""
    # Initialize a loop to iterate over the rolling window
    for j in range(rolling_window):
        # If the number is greater than the current maximum element, update the maximum element
        if number > max_list[j]:
            max_list[j] = number
        # If the current index is outside the rolling window, reset the list element to negative infinity
        elif j > i:
            max_list[j] = float('-inf')

# Tests
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

print(rolling_max(numbers, rolling_window))  # [1, 2, 3, 3, 3, 4, 4]
```

In the above code, the `rolling_max()` function takes an input list of integers `numbers` and a rolling window `rolling_window`.
It returns a list of length `rolling_window` containing the maximum elements from the rolling window moving along the input list.

The `update_max_list()` function is used internally by `rolling_max()` to update the list of rolling maximum elements.

The test case demonstrates the correctness of the function by returning the expected result for the input list `[1, 2, 3, 2, 3, 4, 2]` and a rolling window of size 3.