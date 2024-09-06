```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(sorted(numbers), numbers) if i < numbers[i]]

# Test cases
numbers1 = [1, 2, 3, 4]
numbers2 = [2, 3, 4, 5]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)

print("Result 1:", result1)
print("Result 2:", result2)
```

This script defines a `rolling_max` function that takes a list of integers and returns a new list with the maximum element from the list after each element in the original list. The function uses the method to sort the list and pick the maximum element from each subsequent pair of sorted elements and the original list.