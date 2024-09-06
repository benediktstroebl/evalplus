```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen] * len(numbers)
    for i in range(1, len(numbers)):
        max_seen = max(numbers[i], max_seen)
        result[i] = max_seen
    return result
``` 

This Python script defines a function called `rolling_max` that uses a given list of integers to create a new list of rolling maximum values. The function operates by recording the initial observed maximum value (initially set to the first element of the input list) and generating an initial result list identical in length to the input list, filling it with the recorded maximum value. Then, it proceeds through the input list, updating the maximum value as it goes, and adjusts the corresponding element in the result list. Ultimately, the function returns the updated list with the rolling maximum values. 

Here is an example usage of the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(test_list))
```

The expected output is:
```
[1, 2, 3, 3, 3, 4, 4]
``` 

This demonstrates how the function properly identifies the rolling maximum values, especially when the maximum element changes over time.