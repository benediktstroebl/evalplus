```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The function takes advantage of Python's list comprehension and the max function to easily find the rolling maximum over a given window.