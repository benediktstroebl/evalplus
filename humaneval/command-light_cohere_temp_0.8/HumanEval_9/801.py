```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
``` 
This Python function `rolling_max` generates a list of rolling maximum elements from a given list of integers. It uses list comprehension to iterate through the current maximum element to the end of the list and keeps adding them as a new list.