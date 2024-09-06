```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in sorted((-n, 1), key=lambda x: x[1]) if idx < len(numbers)]
```
This code defines a function called `rolling_max`, which takes a list of integers as input and returns a list of the most frequent element in the sequence. It uses the using a least element to sort the list based on the rolling maximum element. The key function is used to determine the most frequent element in the list, which is essential for the purpose of this code.