```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if x == max(numbers)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
``` 
This function generates a list of integers, starting from the first element and going until it reaches the maximum element in the list. This process is optimized to find the maximum element quickly.