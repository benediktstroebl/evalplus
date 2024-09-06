```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_list = [x for x in numbers if x > maxResult]
    maxResult = max(max_list)[0] if max_list else numbers[0]
    return [maxResult] + max_list[1:]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [2, 3, 4, 5]
numbers3 = [1, 3, 9]
numbers4 = [9999, 2]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)
result3 = rolling_max(numbers3)
result4 = rolling_max(numbers4)

print("Results:", result1, result2, result3, result4)
```
This Python code defines a function `rolling_max` that calculates and returns the rolling maximum elements from a given list of integers. The function utilizes list comprehension to find the maximum element and then adds the maximum element to the beginning of the list. It is tested with four test cases, printing the results for each test.