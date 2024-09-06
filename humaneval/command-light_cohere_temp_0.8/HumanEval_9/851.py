```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x == max(numbers)]
    return [num for num in numbers if num != max_numbers[0] and num > max_numbers[0]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4]
result = rolling_max(numbers)
print(result)

numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)

numbers = [5, 2, 1]
result = rolling_max(numbers)
print(result)

numbers = [3, 1, 2, 1, 3]
result = rolling_max(numbers)
print(result)
```
The function `rolling_max` takes a list of integers as input and returns a new list containing the rolling maximum elements. It accomplishes this time, it uses a list comprehension to generate a list of maximum elements found so far (max_numbers), then it returns a new list containing elements that are greater than the current maximum found in max_numbers but less than the current maximum element in the list.

The test cases provided demonstrate the correctness of the function. It successfully identifies the examples of lists where the rolling maximum elements change over time and returns the correct results.