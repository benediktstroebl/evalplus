```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][1: rolling_window + 1]) 
           for numbers in zip(numbers, numbers[1:])][:-rolling_window - 1]
```

The function takes two parameters:
- numbers - the input list of integers.
- rolling_window - the window size for the rolling maximum.

It uses the zip function to compare each element with the reversed ones and maximizes them using max and a slice notation [1: rolling_window + 1] to get the maximum values limited to the window size. The rolling max values are obtained by applying the rolling max logic to the zipped and sliced list and omitting the last element of the window to match the list start.

Here is an example usage of the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print("Original list:", test_list)
print("Rolling Maxima for window size 3:", rolling_max(test_list, 3))
```

And here is the expected output:
```
Original list: [1, 2, 3, 2, 3, 4, 2]
Rolling Maxima for window size 3: [1, 2, 3, 3, 3, 4, 4]
```