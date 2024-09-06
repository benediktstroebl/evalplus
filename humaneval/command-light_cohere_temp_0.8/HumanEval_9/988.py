```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max and num < max_num:
            max_num = current_max
    return [max_num]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [5, 6, 7, 3, 8, 2]
result2 = rolling_max(numbers2)
print(result2)  # Expected output: [8, 7, 6, 3, 2]

numbers3 = [10, 5, 6, 4, 1]
result3 = rolling_max(numbers3)
print(result3)  # Expected output: [10, 10, 6, 4]
```
This Python code defines a function rolling_max that calculates and returns the maximum element from a given list of integers, it sorts the input list and iterates through it using a rolling window approach to identify the maximum element at each moment. The code also includes several test cases to verify the correctness of the rolling_max function.