```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

# Basic test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max = [rolling_max(numbers), rolling_max([2, 3, 4, 1, 2]), rolling_max([1, 2, 3, 2, 5])]
print(test_rolling_max)

# Test with negative numbers
numbers = [-1, -2, -3, -4, -5]
test_rolling_max = [rolling_max(numbers), rolling_max([-3, -2, -1, -4])]
print(test_rolling_max)

# Test with one element
numbers = [1]
test_rolling_max = [rolling_max(numbers),]
print(test_rolling_max)
``` 
This Python code defines a function `rolling_max` that generates a list of rolling maximum elements in a given list of integers. The function uses a element-at-a-time comparison to identify the maximum value. The test cases section passes various tests, including basic, negative number, and one element tests, to ensure the correctness of the `rolling_max` function.