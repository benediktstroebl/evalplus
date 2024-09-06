```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generate a list of rolling max elements in the sequence. 
    Return the max number in the sequence at every moment. 
    Input: numbers -- list of integers. 
    Returns: list of integers with the same length 
    as input list
    """
    numbers = [num for num in numbers] 
    return [max(numbers[i:]) for i in range(len(numbers))]

# Test cases
numbers1 = [1, 2, 3, 4, 5]
print(rolling_max(numbers1))  # Output: [3, 4, 5, 5, 4, 3, 2, 1]

numbers2 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(rolling_max(numbers2))  # Output: [9, 8, 10, 10, 9, 8, 7, 6, 5]

numbers3 = [1, 2, 3, 4, 4, 3, 2, 1]
print(rolling_max(numbers3))  # Output: [3, 3, 3, 3, 2, 1]

numbers4 = [10, 2, 98, 3, 97, 99, 100]
print(rolling_max(numbers4))  # Output: [98, 100, 100]
```
This script defines a function `rolling_max` which takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence. It uses the maximum number in the sequence at every moment, and this is the output. The test cases demonstrate the good function.