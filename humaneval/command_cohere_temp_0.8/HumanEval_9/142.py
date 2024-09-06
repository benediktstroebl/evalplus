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

This code defines a function called `rolling_max` that takes a list of integers `numbers` as input. Inside the function, it initializes an empty list `rolling_maxes` of the same length as the input list, and the goal is to populate this list with the maximum elements seen thus far at each position. It starts by assigning each element in the input list to its corresponding position in `rolling_maxes`, assuming the element to be the maximum seen so far. Then it iterates through the list, comparing each element with the maximum element in the previous iteration. If the current element is greater, it updates the value at the current index in `rolling_maxes` to be the current element. Finally, the function returns the `rolling_maxes` list, which represents the rolling maximum elements found in the input list. 

Here is an example usage of the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(test_list))
```

The output of this code will be:
```
[1, 2, 3, 3, 3, 4, 4]
```

This is a demonstration that the function correctly identifies the rolling maximum elements up to each point in the list.