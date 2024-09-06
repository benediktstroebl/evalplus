Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence. Maximum elements overlapping with the rolling_max_window are included in the result."""
    if not numbers:
        return []

    assert isinstance(numbers, list), "Input 'numbers' must be a list."
    assert isinstance(rolling_max_window, int) and rolling_max_window > 0, "Input 'rolling_max_window' must be a positive integer."

    result = [num for num in numbers if num == max(set(numbers)[rolling_max_window:]])
    
    return result

# Test cases
numbers_list_test_cases = [
    ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1], [1]),
    ([], []),
]

for numbers, expected_result in numbers_list_test_cases:
    print(f"Input: {numbers}")
    print(f"Expected: {expected_result}")
    print(f"Result: {rolling_max(numbers, 3)}")
    print("="*30)
```

This script defines the `rolling_max()` function, takes a list of numbers and a window size `rolling_max_window` as input, and returns a list of maximum elements found within the rolling window. The function first checks if the input list is empty, returns an empty list if true, and then finds the maximum elements in the current rolling window. The number of elements in the rolling window is given by `rolling_max_window`. The maximum elements overlapping with the rolling window are retained in the result list.

The test cases provided demonstrate how the function works with different inputs and expected results. You can modify these test cases or add more to further validate the functionality of the `rolling_max()` function.