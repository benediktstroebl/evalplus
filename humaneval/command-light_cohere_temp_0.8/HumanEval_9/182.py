```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in zip(numbers, numbers[1:]) if x > numbers[0]]
```
This function, rolling_max, accepts a list of integers and generates a new list with the rolling maximum elements, using a nested loop and a comparison with the first element of the input list. The output list will contain the maximum value in the list, ensuring the list remains unmodified.