```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_maxes[i-1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This script defines a function called `rolling_max`, which takes a list of integers as input and returns a list of rolling maximum elements found in the sequence up to that point. The function starts with copying the input list to `rolling_maxes` and then iterates through each element of the list. It compares each element with its previous element and updates the value of `rolling_maxes` if the current element is greater than the previous one. Finally, it returns the updated `rolling_maxes` list.