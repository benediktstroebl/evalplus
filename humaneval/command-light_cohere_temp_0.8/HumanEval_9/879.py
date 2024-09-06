```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(zip(numbers, numbers[1:])) if num > numbers[0]]

# Test the function with a sample input and expected output
numbers = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(numbers)
print("Test Result:", endswith(test_result))
```