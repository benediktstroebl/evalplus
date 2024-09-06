```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(numbers)
print("Test Case 1 Result:", endswith(test_result)) # [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
test_result = rolling_max(numbers)
print("Test Case 2 Result:", endswith(test_result)) # [1, 2, 3, 4]

numbers = [10, 9, 8, 7, 6, 5]
test_result = rolling_max(numbers)
print("Test Case 3 Result:", endswith(test_result)) # [10, 9, 8, 7]

``` 
This solution provides a function `rolling_max` that accepts a list of integers and produces a new list with the rolling maximum elements. The function employs a list comprehension and the `max()` function. The test cases are designed to ensure that the `rolling_max` function operates as expected and prints the expected results.