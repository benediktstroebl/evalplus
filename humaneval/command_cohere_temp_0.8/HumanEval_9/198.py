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

This Python script defines a function called `rolling_max` that uses a given list of integers to generates a new list of rolling maximum elements encountered in the sequence up to that point. The function takes a parameter called `numbers`, which is a list of integers, and returns a list of integers.

The process involves maintaining a `max_seen` variable that stores the maximum value observed so far. Initially, it's set to the first element of the sequence. The `result` list is then initialized with this first maximum. As the loop iterates through the rest of the sequence, each element is compared with the `max_seen`. If it's greater, the `max_seen` is updated. Otherwise, the current value of `max_seen` is appended to the `result` list. Ultimately, the `result` list contains a sequence of rolling maxima, where each maximum represents the highest value encountered thus far during the iteration. 

This script provides a useful utility to effortlessly extract rolling maxima from a sequence of integers.