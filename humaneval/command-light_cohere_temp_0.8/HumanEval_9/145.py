```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(sorted(numbers), range(len(numbers))) if i < len(numbers)]

# Test case using markdown code block for output:
test_data = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(test_data)
print(f"Test Results: {test_result}")
```
This function, rolling_max, uses the list's built-in sorting method and a for loop to locate the list's rolling maximum element. The function then returns the first member of the list that matches the rolling maximum criterion, which is how the function is tested.