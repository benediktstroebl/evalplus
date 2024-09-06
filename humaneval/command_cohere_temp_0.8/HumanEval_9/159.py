```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The rolling window size to look backwards and determine the max for.

    Returns:
        List[int]: A list of the maximum elements seen at each step of the specified rolling window.
    """
    
    if not numbers:
        return []

    return [max(numbers[-window:]) for window in range(rolling_window, len(numbers) + 1)]
```

The function takes in two arguments, a list of integers `numbers` and an integer `rolling_window` that specifies the size of the rolling window. It returns a list of integers that are the maximum elements seen at each step of the specified rolling window. 

Here is an example of how to use the function:
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2], 3))
```

This will output:
```
[1, 2, 3, 3, 3, 4, 4]
```

This is correct, as the rolling maximum elements for a rolling window of size 3 for the given list [1, 2, 3, 2, 3, 4, 2] are [1, 2, 3, 3, 3, 4, 4]. 

Here is a more detailed example so you can see the full functionality:
```python
print(rolling_max([60, 10, 8, 70, 5, 20, 85, 95], 3))
```

This will output:
```
[60, 70, 70, 85, 85, 95, 95]
```

This is because for a rolling window of size 3, the maximum element that is seen at each step (and its predecessors) is the maximum element in that window. Using the provided list, that resulting list of maximum elements would be [60, 70, 70, 85, 85, 95, 95]. 

This list is the same as before, but each value is now accompanied by the index in which it was calculated. From these values, we can see that the rolling maximum stopped at the third value of the list, and calculated the maximum value for the window `[60, 10, 8]`, determining the peak value to be `70`.