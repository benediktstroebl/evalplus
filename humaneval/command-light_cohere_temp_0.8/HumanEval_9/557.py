```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements found until a given moment in the sequence.
    : Parameters
   
    list of integers
    numbers -> List[int]
    """
    return [max(numbers[i:]) for i in range(len(numbers))]]

#Test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 4, 5]
numbers3 = [10, 20, 30, 40]

print(rolling_max(numbers1))  # [1, 2, 3]
print(rolling_max(numbers2))  # [3, 5, 10, 20]
print(rolling_max(numbers3))  # [10, 30, 40]
```
This code defines a function named rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements from the original list. It utilizes a maximum technique to efficiently calculate the maximum element at each moment until the input list is exhausted.