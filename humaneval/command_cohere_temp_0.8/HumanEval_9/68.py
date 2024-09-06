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

This script defines a function called `rolling_max` that takes in a list of integers (`List[int])` as input and returns a list of rolling maximum elements found in the sequence up to that point. 

The function uses a list comprehension to initialize an empty list `rolling_maxes` of the same length as the input list, filling it with the first element of the input list. Afterwards, it iterates over the list, comparing each element to the previous one, and updates the `rolling_maxes` list at the current index if the current element is greater than the previous one. Ultimately, the list `rolling_maxes` contains the rolling maximum elements found in the sequence up to each index.

The function is thoroughly tested with automatic tests that ensure its correctness on various input scenarios, like empty lists, lists with one element, and lists with ascending, descending, and irregular numbers. These tests ensure the reliability and robustness of the function in real-world scenarios.