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

This code defines a function called `rolling_max` that takes a list of numbers as input and returns a list of the rolling maximum elements found in the sequence up to each index. It initializes an empty list `rolling_maxes` of the same length as the input list to store the rolling maximums. It then uses a list comprehension to populate the `rolling_maxes` list with the original input values. The code then enters a loop that iterates through the list, comparing each element to the previous one. If the current element is greater than the previous one, it updates the value at the corresponding index of the `rolling_maxes` list with the current element, effectively keeping track of the rolling maximums. Finally, it returns the `rolling_maxes` list.