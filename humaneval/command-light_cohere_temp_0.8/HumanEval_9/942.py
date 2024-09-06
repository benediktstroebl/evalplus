```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_index = i
    return [max_num]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This function, rolling_max, takes a list of integers as input and returns a new list containing the rolling maximum element. The function uses a algorithm that keeps track of the maximum element seen so far and iterates through the list. 

The algorithm works by comparing each element with the current maximum, and if the element is larger, it updates the maximum and its index.

This is a simple implementation of the rolling maximum algorithm that can be used to find the maximum element in a list of integers.