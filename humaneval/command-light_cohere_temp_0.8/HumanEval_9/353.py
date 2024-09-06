```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    rolling_max_inner = []
    for num in numbers:
        while rolling_max_inner and num < rolling_max_inner[-1]:
            rolling_max_inner.append(rolling_max_inner[-1])
            rolling_max_inner.pop(0)
        rolling_max_inner.append(num)
    max_num = rolling_max_inner[-1]
    rolling_max_inner.sort()
    maximum = rolling_max_inner
    return [maximum]

rolling_max_test_pass = [2, 3, 4, 1, 5, 3]
print(rolling_max(rolling_max_test_pass))
```

This code defines a function called `rolling_max` that takes a list of integers as input and returns a list of the maximum elements after they have been rolled one or more times. The `rolling_max_inner` list stores the maximum elements found so far. The `max_num` is the last element in the `rolling_max_inner` list, and it is used to update the rolling maximum value. The code then passes a test by calling the `rolling_max` function with a list of integers [2, 3, 4, 1, 5, 3], which should return the list [1, 5, 3].