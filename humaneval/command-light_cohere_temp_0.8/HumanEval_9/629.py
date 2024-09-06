```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted((num for num in numbers if num > 0), reverse=True)]

# Test cases
numbers1 = [1, 2, 3, 4, 5]
assert rolling_max(numbers1) == [5, 4, 3, 3, 2]

numbers2 = [1, 2, 3, 0, 4]
assert rolling_max(numbers2) == [1, 2, 3]

numbers3 = [0, 1, 2, 3, 4]
assert rolling_max(numbers3) == [0, 1, 2]

numbers4 = [1, 2, 3, 4, 4]
assert rolling_max(numbers4) == [4, 4]

numbers5 = [1, 2, 3, 4, 5, 6]
assert rolling_max(numbers5) == [4, 3, 2]
```
This Python script provides a self-contained function `rolling_max` that takes a list of integers as input and returns the list of the maximum elements after applying a sorting algorithm with a reverse order. The test cases aim to validate the correctness of the `rolling_max` function by passing different types of input data and verifying if the returned values match the expected results.