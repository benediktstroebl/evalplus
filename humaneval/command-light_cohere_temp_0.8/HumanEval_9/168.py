Here is a self-contained Python script that solves the given problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [num for num in numbers if num > maxnum]
    maxnum = max(max_numbers) if max_numbers else numbers[0]
    return [maxnum] + max_numbers[1:]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Expected output: [3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
print(rolling_max(numbers))  # Expected output: [5, 5, 5]

numbers = [10, 20, 30, 40, 10]
print(rolling_max(numbers))  # Expected output: [10, 10, 30, 40]
```
This script defines a function `rolling_max` which generates a list of rolling maximum elements from a given list of integers. The function uses a max element of a list until a non-increasing number is found.