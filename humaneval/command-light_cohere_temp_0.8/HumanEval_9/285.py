```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), range(len(numbers))) if idx == numbers.count(max(numbers))]
``` 
This function takes a list of integers and returns a list of the rolling maximum elements. The function uses the max function to find the maximum element in the list and uses the `count` function to determine the index of the maximum element.