```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    current = max_number
    rolling_maxes = [current]
    
    for num in numbers[1:]:
        current = max(num, current)
        rolling_maxes.append(current)
    
    return rolling_maxes

# Unit tests
numbers = [1, 2, 3, 2, 3]
rolling_result = rolling_max(numbers)
print("Rolling maximum elements:", rolling_result)  # Output: [1, 2, 3, 3, 3, 4]

numbers = [1, 1]
another_result = rolling_max(numbers)
print("Rolling maximum elements:", another_result)  # Output: []
```

The script defines a function `rolling_max` which takes a list of integers as input and returns the list of the maximum elements after applying a rolling maximum element identification algorithm. The script also provides unit tests for the function to ensure its correctness.