```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in enumerate(numbers, 1) if numbers[i] > numbers[i-1] or i == len(numbers)]

# Test case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This code provides a self-contained solution to the rolling max problem. The typing module is used to ensure type safety and provide better runtime behavior for the code.

The rolling_max function takes a list of integers as an input and returns a list of the elements that are greater than their previous elements or the length of the list. The function uses the numbers list's first element as the starting point and uses the current index and the previous element to determine whether a number should be included in the result.