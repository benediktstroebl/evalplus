```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_maxes[i-1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

The provided code defines a function called `rolling_max` that takes a list of integers as input. Inside the function, it initializes an empty list called `rolling_maxes` of the same length as the input list, which will store the rolling maximum elements. Then it iterates through the list, comparing each element with its previous element, and updates the `rolling_maxes` list whenever a larger element is encountered. The function ultimately returns the modified `rolling_maxes` list, containing the rolling maximum elements from the original list.