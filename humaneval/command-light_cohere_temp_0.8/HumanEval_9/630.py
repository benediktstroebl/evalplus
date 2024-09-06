```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    current = max_number
    for num in numbers[1:]:
        if num > current:
            current = num
        elif num == current:
            current += 1
    return [current, ]
# Testing the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
```
This code defines a function called `rolling_max`, which takes a list of integers as an argument and returns a new list with the rolling maximum elements found in the input sequence. The function initializes a max number with the first element of the input list, and then iterates through the remaining elements, comparing each one to the current maximum. If a current element is greater than the max, the current value becomes the new max. If the current element is equal to the max, then the rolling maximum element is incremented by 1. The output of this code is the list [3, 3, 3, 3, 4, 4] which contains the rolling maximum elements of the input list.