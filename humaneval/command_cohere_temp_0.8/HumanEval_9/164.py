```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen]
    for n in numbers[1:]:
        if n > max_seen:
            max_seen = n
        result.append(max_seen)
    return result
``` 

The Python script defines a function called `rolling_max` takes a list of integers `numbers` as input and returns a list of rolling maximum elements found in the sequence up to that point. Initially, the maximum seen is set to the first element of the list. As the loop iterates through the list, it compares each element to the maximum seen so far, updating it if the element is greater. At the same time, the maximum seen is appended to the `result` list. As a result, the `result` list contains the rolling maximum elements, whereas the last value reflects the maximum element seen so far while iterating through the list.  This approach allows you to efficiently calculate and return the rolling maximum elements within the list, providing insight into the local maximum values observed across the sequence.