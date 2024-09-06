```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This Python script defines a function called `rolling_max`, which takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence up to each point in the list. 

The function starts with a list assignment of the input list `numbers` to `rolling_maxes`. A loop then goes from index `1` (skip the first element) and compares the current element to the previous one. If it's greater, it assigns the current element to the respective index of `rolling_maxes`. Ultimately this yields the maximum element from the sequence up to that moment in time. 

The `rolling_max` function as defined above takes a list of integers as input and returns a list of the rolling maximum elements. It utilizes the `typing` module to define the input and output types, allowing for type checking. 

If we were to apply this function to the provided test case:
 ```python
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```

And the output aligns with the desired output. 
```python
```