```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    out = []
    maxes = []  # to store the rolling maximums so far
    for num in numbers:
        if maxes == []:
            maxes.append(num)
            out.append(num)
        else:
            if num > maxes[-1]:
                maxes.append(num)
                out.append(num)
            else:
                if num == maxes[-1]:
                    out.append(maxes[-1])
                else:
                    maxes.append(num)
                    out.append(num)
    return out
```

The algorithm uses a "two pebbles in a bucket" approach. Two elements are maintained - one is the current maximum and the other is the maximum encountered so far. Every subsequent element is compared against both values and appropriate updates are made.