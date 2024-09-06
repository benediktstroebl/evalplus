Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(window)) for window in zip_longest(numbers, numbers[1:]+[None])][:-rolling_window]

def zip_longest(*args) -> List[Tuple[object]]:
    return list(zip_longest(*args))

# Test Cases
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

expected = [1, 2, 3, 3, 3, 4, 4]
got = rolling_max(numbers, rolling_window)

assert expected == got
```

This script defines a `rolling_max` function that takes a list of numbers and a rolling window parameter, and iteratively calculates the maximum element in the rolling window. The function uses `zip_longest` to iterate over overlapping windows of the list, excluding the last `rolling_window` elements, and maximizes each window. The `zip_longest` function is also included, which handles variably sized arguments during zip execution, using None as a placeholder for missing values. Test cases are provided to validate the functionality of the rolling_max function against the expected result.