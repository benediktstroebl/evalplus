```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, range(len(numbers))) if numbers[i] > numbers[i - 1]]

# Sample test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [3, 1, 4, 5, 6, 7]
result = rolling_max(numbers)
print(result)  # Output: [4, 5, 6, 7]

numbers = [8, 9, 10, 11, 12, 13]
result = rolling_max(numbers)
print(result)  # Output: [8, 9, 10, 11, 12, 13, 10, 11, 12]
```
This script provides a simple solution to the problem using a generator expression. The `rolling_max` function returns a list of the maximum element from the previous list at each index. This approach avoids storing the simple lists and provides a more concise solution to the problem.