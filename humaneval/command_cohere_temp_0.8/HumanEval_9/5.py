Here's a Python script that contains a function called `rolling_max` which takes a list of numbers and returns a list of rolling maximum elements from the list:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], optional_window_size: int = 1) -> List[int]:
    if not numbers:
        return []

    if optional_window_size == 1:
        return [max(numbers[i], numbers[i-1]) for i in range(1, len(numbers))]
    else:
        return [max(numbers[i-window_size:i+1]) for i in range(window_size, len(numbers))]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

The function takes a list of numbers as input and an optional parameter window_size which defaults to 1. It uses Python's maximum function and generator expression to find the rolling maximum elements in the list.

To test the function, we provide a sample list of numbers and print the function output to verify its correctness. 

**NOTE:** The original problem statement did not specify the window size, we added a default parameter to the function to cover both cases. If a specific window size is required, it can be passed to the function during usage.