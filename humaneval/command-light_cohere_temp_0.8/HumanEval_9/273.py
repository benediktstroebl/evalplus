```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n,i in reversed(enumer())][::-1:]
```
Here's a self-contained Python function that solves the rolling max problem. The code uses the only one line: it creates a list with the last value of each number in the list as the maximum. The list is then reversed and then reversed again to get the correct order of the rolling maximum elements.