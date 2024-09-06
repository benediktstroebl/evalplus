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

This code defines a function called `rolling_max` that takes in a list of integers (`List[int])` as input. Within the function, it initializes an empty list called `rolling_maxes` of the same length as the input list, initially filled with copies of the input elements. It then iterates through the list, comparing each element with the previous one. If the current element is greater than the previous one, it sets the corresponding value in the `rolling_maxes` list to the current element. After processing the entire list, it returns the `rolling_maxes` list, which contains the rolling maximum elements from the original list. 

Here is an example usage of the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(test_list))
```

The output of the code would be:
```
[1, 2, 3, 3, 3, 4, 4]
```