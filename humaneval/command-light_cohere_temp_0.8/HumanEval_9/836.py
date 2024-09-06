```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sublist(numbers)
    return [max(numbers[i]) for i in range(len(numbers))]]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```
This function uses the `max` function to return the maximum element in a list of numbers. It also uses the`sublist` to iterate over the list and get the maximum value for each moment.