```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This code snippet uses a list comprehension to initialize a rolling_maxes list that mirrors the input list numbers. The nested for loop compares each element in numbers with its previous element, updating the corresponding rolling_maxes element if the current element is greater. This generates a list of rolling maximum elements up to that point in the sequence. The function returns this rolling_maxes list.