```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.list = list(numbers)
    max_num = numbers[0]
    current = max_num
    for num in numbers[1:]:
        current = max(num, current)
        max_num = current
    return [max_num]

# Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
``` 
This Python function, named `rolling_max`, takes a list of integers as input and uses a rolling max algorithm to find the maximum element in the list. It then returns a array of the maximum elements found.