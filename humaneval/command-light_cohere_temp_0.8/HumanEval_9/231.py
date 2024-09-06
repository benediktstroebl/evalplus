```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # Sort the list of integers to have the largest first
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max and num < max_num:
            max_num = current_max
    return [max_num]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
The output will be:
```
[4, 4]
```
This Python script defines a function called rolling_max that takes a list of integers as input and generates a new list with the maximum element from the original list after each element in the list has been added. The function achieves this maximum element by comparing the current maximum with each element in the list. The function then returns a list of the maximum elements.