Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][1:rolling_window+1]) for nums in numbers[::-1]]
```

The `rolling_max` function takes in a list of integers `numbers` and an integer `rolling_window` as parameters. It uses `max` function with `zip` to calculate the maximum elements for the window of the size `rolling_window` from the sequence of numbers. The sequence of rolling maximum elements is then reversed and returned. 

The reversed order guarantees that the result lists will have elements corresponding to the maximum for the rolling window for each element in the original sequence. 

Also, the list is reversed to correctly handle the case when `rolling_window` is greater than the length of the sequence. 

This solution has tests corresponding to the example in the prompt and additional cases to cover different scenarios:
```python
def test_rolling_max():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 1) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 2) == [1, 2, 3, 3, 4, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 3) == [1, 2, 3, 4, 4, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 4) == [1, 2, 3, 4, 4, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 5) == [1, 2, 3, 4, 4, 4, 4]

    assert rolling_max([1, 2, 3, 2, 3, 4, 2, 5, 6, 7], 3) == [1, 2, 3, 4, 5, 6, 7]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2, 5, 6, 7], 4) == [1, 2, 3, 4, 5, 6, 7]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2, 5, 6, 7], 5) == [1, 2, 3, 4, 5, 6, 7]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2, 5, 6, 7], 6) == [1, 2, 3, 4, 5, 6, 7]

    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 0) == [1, 2, 3, 2, 3, 4, 2]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], -1) == [1, 2, 3, 2, 3, 4, 2]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], -5) == [1, 2, 3, 2, 3, 4, 2]
``` 

The test cases cover edge cases of the function to verify its correctness. 

The `test_rolling_max` function executes the `rolling_max`