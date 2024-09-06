```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x > max_num]
    max_num = max(max_numbers)
    return [max_num]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [3, 3, 3, 3, 4, 4]
```
This Python code defines a function `rolling_max` that takes a list of integers as input and returns a list of the largest elements from the input. It achieves this by iterating through each element in the list to find the current maximum and keeps track of the largest element using the `max_numbers` list. The final result is a list of the largest elements in the input list.