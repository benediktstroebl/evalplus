```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers. rollover = [nums.rolling_max([1, 2, 3, 4])
    return [x for x in numbers if x >= rolling_max(numbers[1:])][::-1]]

rolling_max_test = [1, 2, 3, 4, 5]
result = rolling_max(rolling_max_test)
assert list(result) == [1, 2, 3, 3, 3, 4]

rolling_max_test2 = [1, 2, 3, 4, 5, 6]
result2 = rolling_max(rolling_max_test2)
assert list(result2) == [1, 2, 3, 4]
```
This script defines a function `rolling_max` which takes a list of integers as input and returns a list of the largest elements from the list, as a rolling maximum. The function uses an "rolling" principle to calculate the rolling maximum element in the list. It also has a test cases to verify the correctness of the function. The test cases are self-contained within the function.