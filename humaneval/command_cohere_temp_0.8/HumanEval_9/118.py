```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen]
    for num in numbers[1:]:
        if num > max_seen:
            max_seen = num
        result.append(max_seen)
    return result
``` 

This Python script defines a function called `rolling_max` which takes a list of integers as an argument and returns a list of the maximum integers encountered thus far in the sequence. The function starts by setting the `max_seen` to the first element of the list and creates a list result containing this value. It then iterates over the remaining elements in the list, if an element is greater than the `max_seen`, it is updated to this new value. Regardless, the current `max_seen` is appended to the `result` list. After processing all elements, the function returns the `result` list which contains the rolling maximum elements seen in the order they appeared in the original list. 

Here is an example usage of the function:
```python
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```
This will return a list of rolling maximum elements seen in the order they are encountered in the sequence.