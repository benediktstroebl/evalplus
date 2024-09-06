```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This script defines a function called `rolling_max` that takes a list of integers `numbers` as input. It returns a new list where each element represents the maximum value encountered so far as you move through the sequence from left to right. The function starts with copying the input list to `rolling_maxes`, and then it iterates through the list, updating each element to the right of the current element if the current element is greater than the previous one. Ultimately this builds a list of rolling maximums.