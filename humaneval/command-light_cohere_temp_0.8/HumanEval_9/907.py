```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Test cases for rolling_max function
numbers_test = [1, 2, 3, 2, 3, 4, 2]
result_test = rolling_max(numbers_test)
assert list(result_test) == [1, 2, 3, 3, 3, 4, 4]

lists_of_numbers = [ [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 7, 8, 9]]
result_lists = [rolling_max(numbers) for numbers in lists_of_numbers]
assert all(result_lists == [max(numbers) for numbers in each])
```  This code defines a function called rolling_max that takes a list of integers as input and returns a new list of integers that contains the maximum element from each rolling window of the input list. The code also includes test cases to verify the correctness of the rolling_max function.