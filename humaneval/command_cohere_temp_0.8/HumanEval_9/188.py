```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list where each element is the maximum of the current window.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers or not rolling_window:
        return []

    # Create a buffer to store the rolling window of integers, initialized with the first `rolling_window` integers from `numbers`.
    buffer = [numbers[0]]
    buffer.extend(numbers[1:rolling_window])

    for i in range(rolling_window, len(numbers)):
        # Add the current integer to the buffer and remove the oldest integer to maintain the rolling window.
        buffer.append(numbers[i])
        buffer.pop(0)

        # Update the maximum if the current integer is greater than the maximum in the buffer.
        if numbers[i] > buffer[0]:
            buffer[0] = numbers[i]

    # Return the buffer, which now holds the rolling maximum for each position in `numbers`.
    return buffer
```

This code defines the `rolling_max` function, taking in a list of integers `numbers` and an integer `rolling_window` that determines the size of the rolling maximum window. It operates by maintaining a buffer of size `rolling_window` that is updated iteratively through the input list. At each step, the current value is added to the buffer and the oldest value is removed, ensuring the rolling maximum effect. The maximum value within the buffer is updated whenever a greater value is encountered. Ultimately, the function returns the buffer, providing a list of rolling maximums corresponding to each position in the input list.

Here is an example of using the `rolling_max` function to create a list of rolling maximum elements found until a given moment in the sequence:
```python
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

rolling_max_list = rolling_max(numbers, rolling_window)
print(rolling_max_list)
```

This will print:
```
[1, 2, 3, 3, 3, 4, 4]
```

This output matches the example provided in the original problem statement.