```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_numbers = [current_max]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_count += 1

    if max_count == len(numbers):
        max_numbers.else elements max_numbers[-1]
    else:
        max_numbers.append(current_max)
        current_max = numbers[-1]
        max_numbers.append(current_max)

    return max_numbers

# Test cases
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
numbers3 = [10, 20, 30]

result1 = rolling_max(numbers1)
print(result1)  # Expected output: [1, 2, 3, 4]

result2 = rolling_max(numbers2)
print(result2)  # Expected output: [5, 6, 7, 8]

result3 = rolling_max(numbers3)
print(result3)  # Expected output: [10, 20, 30]
```
The function rolling_max calculates and returns the list of rolling maximum elements from a given list of integers, based on the input test cases.