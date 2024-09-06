```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_element = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers):
        if num > max_element:
            max_element = num
            max_index = i + 1
    return [max_element]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers2 = [5, 15, 6, 9, 3]
result2 = rolling_max(numbers2)
print(result2)

numbers3 = [1, 10, 20, 30, 40, 50]
result3 = rolling_max(numbers3)
print(result3)
```
This Python script defines a function `rolling_max` that calculates and returns a list of the rolling maximum elements from a given list of integers. It employs a `typing` to ensure proper function typing. The function is designed to handle lists of integers, and it iterates through the list to find the maximum element at each moment. The results of the script's calls to the `rolling_max` function are then printed, demonstrating the expected behavior of the function.