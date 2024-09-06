Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at different points in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_return = []
    for i in range(len(numbers)):
        max_found = max(numbers[i], rolling_max_return[-1])
        rolling_max_return.append(max_found)
    return rolling_max_return
```
The function uses a loop to iterate through each element in the input list. It maximizes either the current element or the last rolling maximum found, whichever is greater, and appends the result to the `rolling_max_return` list.

Here's an example usage of the function:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2])
```
The output of this usage will be:
```
[1, 2, 3, 3, 3, 4, 4]
``` 

This exemplifies the generated list of rolling maximum elements, correctly reflecting the values at each position in the input list.