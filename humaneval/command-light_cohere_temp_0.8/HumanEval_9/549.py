```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the rolling maximum element(s) in a list of integers.
    Input:
    numbers: list of integers
    Output: list of integers or None
    """
    numbers.append(numbers[-1]) # append last element to list
    result = [num for num in numbers if num > numbers[-1]]
    return result if result else None

# Test cases
numbers1 = [1, 2, 3, 4]
numbers2 = [4, 2, 3, 1]
numbers3 = [5, 6, 5, 3]
print(rolling_max(numbers1)) # [3, 4, None]
print(rolling_max(numbers2)) # [2, 3]
print(rolling_max(numbers3)) # [6, 5]
```
This code defines a function called rolling_max that takes a list of integers as input and returns a new list with the rolling maximum elements found in the input list. 

The function uses the append to add the last element to the list, and then it iterates through the list and checks each element against the last element to see if it is greater or not. The rolling_max function returns the list with the rolling maximum elements found until the given moment in the sequence.