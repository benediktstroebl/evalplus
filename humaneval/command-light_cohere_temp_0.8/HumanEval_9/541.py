```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements from the given list
    """
    max_window = [num for num in numbers]
    for i in range(1, len(numbers)):
        max_window[i] = max(max_window[i - 1], numbers[i])
    return max_window

# Test cases
test_data = [1, 2, 3, 2, 3, 4, 2]
test_results = rolling_max(test_data)
print("Test Results:", test_results)
```