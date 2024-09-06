```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted((num for num in numbers), reverse=True)]

# Test cases:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print("Rolling maximum:", result)

numbers = [1, 2, 3, 4, 5, 6]
result2 = rolling_max(numbers)
print("Rolling maximum:", result2)

numbers = [10, 20, 30, 40, 10]
result3 = rolling_max(numbers)
print("Rolling maximum:", result3)
```
The output of the code will show the list of the maximum elements found while descending through the list.

This script uses the typing module and defines a function called rolling_max, which takes a list of integers as input and returns a list of the maximum elements found in that list. The test cases show how the essential this function works by passing the test and the result of each test.

It can be an excellent starting point for handling problems in Python that involve working with sequences of data and determining the maximum elements.