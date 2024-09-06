```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen] * len(numbers)
    for i in range(1, len(numbers)):
        max_seen = max(max_seen, numbers[i])
        result[i] = max_seen
    return result
```

The `rolling_max()` function takes a list of integers as input and returns a list of rolling maximum elements found in the sequence up to that point. It starts by initializing `max_seen` to the first element of the input list and creates an initial list of rolling maximums based on this initial maximum. Then, it iterates through the input list, updating `max_seen` as necessary to account for changes in the rolling maximum. The output list is returned with the updated rolling maximums. 

This approach ensures that the function is efficient by only iterating through the input list once and uses sensible variable naming to make the code more readable and maintainable.