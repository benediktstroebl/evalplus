```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:j]) for i, j in zip(range(len(numbers)), numbers[1:j+1])]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [2, 3, 4]
numbers3 = [1, 2, 3, 4, 5]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)
result3 = rolling_max(numbers3)

print("Test Case 1:", result1)
print("Test Case 2:", result2)
print("Test Case 3:", result3)

```
This Python script defines a function `rolling_max` that generates a list of rolling maximum elements within a given list of integers. The function uses a `zip` function and a list slicing technique to iterate through the input list and find the maximum element at each moment. The script provides three test cases with different lists of integers and outputs the results of the `rolling_max` function for each test case.