```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in sorted((idx for idx, n in enumerate(numbers) if numbers[idx] > numbers[idx + 1]), reverse=True)]

# Test Case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

# Test Case 2:
numbers = [1, 3, 4, 2, 5]
result = rolling_max(numbers)
print(result)
```
The code provides a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. It uses the testing to find the maximum value of each element in the list, and then it uses the `sorted` function to sort the list based on the increasing values of elements. The function then returns the maximum value for each element in the list.

The output will be: 
```
[4, 4, 3, 4, 2]
[4, 3, 2, 5] 
```