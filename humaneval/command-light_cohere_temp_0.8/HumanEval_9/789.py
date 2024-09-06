```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return [max_number]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers2 = [1, 20, 9, 8, 3, 10, 2]
result2 = rolling_max(numbers2)
print(result2)
```
The code defines a function named `rolling_max` that accepts a list of integers as an argument and outputs a list of the maximum elements found while rolling over the input list. The code then demonstrates the both the list with different numbers and the result of the `rolling_max` function call for these lists.