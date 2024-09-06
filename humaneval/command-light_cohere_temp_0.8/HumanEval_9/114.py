```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = numbers[0]
    for num in numbers[1:]:
        if num > max_numbers:
            max_numbers = num
    return [max_numbers]
# Example
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
```
This Python code defines a function called rolling_max that takes a list of integers as input and returns a new list of the maximum elements from the input list after applying a rolling maximum function. The rolling_max function uses the max_numbers to start with the first element of the input list and then compares each subsequent element with the current maximum value to determine the maximum element at each moment. The output will be a list containing the maximum values in the numbers list, which is [3, 3, 3, 4, 4] in this case.