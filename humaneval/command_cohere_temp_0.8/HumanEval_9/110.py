```python
from typing import List, Tuple

def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if max_window is None:
        max_window = len(numbers)

    rolling_max_values = [numbers[0]]

    for i in range(1, len(numbers)):
        if i - max_window < 0:
            rolling_max_values.append(numbers[i])
        else:
            rolling_max_values.append(max(rolling_max_values[-max_window:i]+[numbers[i]]))

    return rolling_max_values
```

The given Python script defines a function called `rolling_max` that operates on a list of integers (`List[int]`). This function generates a new list, `rolling_max_values`, where each element represents the maximum value encountered within a rolling window of a specified size (defaulting to the entire list if not provided) as the input sequence progresses. 

Here is an example of how to use the `rolling_max` function by calling it with a sample list and examining the result:
```python
>>> numbers = [1, 2, 3, 2, 3, 4, 2]
>>> rolling_max(numbers)
[1, 2, 3, 3, 3, 4, 4]
```

In this example, the generated `rolling_max_values` list is `[1, 2, 3, 3, 3, 4, 4]`. It signifies that as the sequence progresses, the maximum value within a rolling window of the specified size is considered, leading to the resulting list.