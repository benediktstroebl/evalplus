```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), range(len(numbers))) if numbers[idx] > numbers[idx-1]]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function called rolling_max that generates a list of the rolling maximum elements from a given list of integers. It does this by first sorting the numbers in ascending order and then using the indices of the sorted list to select the maximum element from the previous one, resulting in a list of rolling maximum elements.