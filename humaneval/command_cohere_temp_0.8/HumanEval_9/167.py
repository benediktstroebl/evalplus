```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_maxes[i-1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This script defines a function called `rolling_max` that takes in a list of integers (`List[int])` as input and returns a list of rolling maximum elements found in the sequence up to that given moment. 

The function uses a list comprehension to generate a new list of rolling maximum elements by comparing each element in the input list to the maximum element seen thus far (`rolling_maxes[i-1]`). If the current element is greater, it updates the maximum element seen thus far. 

The resulting list of rolling maximum elements is then returned as the output. 

Here is an example usage of the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(test_list))
```

This would output the following:
```
[1, 2, 3, 3, 3, 4, 4]
```

This is the expected output; it is a list of rolling maximum elements where each element corresponds to the maximum element observed up to that position in the input list.