Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given point in time in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_vals = []
    for i in range(len(numbers)):
        max_vals.append(max(numbers[i:i+2]))
    return max_vals
```
The script uses a simple iterative approach that computes the maximum value for a rolling window of size 2 (that covers the current element and the next element). This logic is then repeated for each element in the input list. 

The script includes type annotations provided in the original prompt: `rolling_max` takes a list of integers `List[int]` as input and returns a list of integers `List[int]`. These types can be used with Python's type hinting system to provide better documentation and code clarity.