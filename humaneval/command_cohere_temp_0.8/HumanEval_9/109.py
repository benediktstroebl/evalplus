```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The `rolling_max` function takes in a list of numbers `numbers` and an integer `rolling_window` as inputs, it returns a list where each element is the maximum value of the sublist consisting of elements `numbers[i-rolling_window:i+1]` for each index `i`.

The following example:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
```
will return:
```
[1, 2, 3, 3, 3, 4, 4]
```
The output lists the maximum value for the sliding window of the size of 3 starting from the first element to the last element in the given list.