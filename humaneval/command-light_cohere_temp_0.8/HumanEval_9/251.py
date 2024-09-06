```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers, reverse=True) if x >= numbers[-1]] + [numbers[-1]]
```
I hope this script provides a self-contained function that solves the problem. It uses the specific typing to provide more clarity and better understandability. The function returns a list of rolling maximum elements found until the last moment in the sequence. 

Would you like assistance with anything else related to Python programming?