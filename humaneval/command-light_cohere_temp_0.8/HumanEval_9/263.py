```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.rolling_max(numbers)
    return numbers

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```
This code provides a self-contained solution to the problem. It defines a function rolling_max that takes a list of integers and returns a new list with the rolling maximum elements.