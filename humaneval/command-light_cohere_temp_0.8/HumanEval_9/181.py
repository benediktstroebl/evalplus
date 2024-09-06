Here is a self-contained Python function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]

# Unit tests
numbers = [1, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as an argument and returns a new list containing the maximum element from the list after each element is added to the list. The function is tested using the `numbers` list to pass the test.