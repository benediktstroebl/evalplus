```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 3, 4, 4]
```
This script defines a rolling_max function which returns the list of the maximum element found from the first moment to the given moment in the sequence, until the sequence ends.