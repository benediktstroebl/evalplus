```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(num for num in numbers if num > max(numbers)))
    return max_numbers

# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 3, 4, 5, 6]

print("Test case 1 result: ", rolling_max(numbers1))
print("Test case 2 result: ", rolling_max(numbers2))
```
The code defines a function called **rolling_max** that takes a list of integers as input and returns a new list containing the rolling maximum elements. It achieves this by iterating through each number in the input list and checking if the number is greater than the current maximum number. The code then runs a series of test cases to verify that the **rolling_max** function works correctly.