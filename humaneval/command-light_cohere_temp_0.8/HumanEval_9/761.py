```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:i]) for i in range(len(numbers))];

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
``` 
This function will return the list containing the maximum element from the numbers list at each moment of the sequence.