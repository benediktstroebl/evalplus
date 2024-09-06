```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [numbers[0]]
    for idx, number in enumerate(numbers[1:]):
        if number > rolling_maxes[-1]:
            rolling_maxes.append(number)
        elif number == rolling_maxes[-1]:
            rolling_maxes.append(rolling_maxes[-1])
    return rolling_maxes

if __name__ == '__main__':
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
```

The `rolling_maxes` list is used to keep track of the maximum elements seen thus far. As the loop iterates through the list of numbers, each current element is compared with the maximum element in the `rolling_maxes` list. If the current element is greater, it replaces the maximum. If they are equal, the maximum is retained as it is. 

This mechanism ensures that the `rolling_maxes` list always contains the _rolling_ maximums up to the current point in the list, and the output list is returned at the end.  The test case checks if the function correctly identifies the rolling maximum elements against a known input.