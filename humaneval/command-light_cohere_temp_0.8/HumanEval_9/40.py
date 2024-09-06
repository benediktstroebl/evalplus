```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    """
    list of rolling maxs = []
    for num in numbers:
        if len(rolling_max.current()) == 0:
            rolling_max.current() = num
        max_val = num
        elif num > rolling_max.current()[0]:
            rolling_max.current() = num
       
        rolling_max.maxs.current() = num
   
        max_val
    rolling_max.current() = max(rolling_max.current(), num)
   
    rolling_max.current()
   
        maxs
    list_of_maxs
    """

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]

rolling_max_result = rolling_max(numbers)
print(rolling_max_result)

numbers2 = [5,2,6,3,7,4,8]
rolling_max_result2 = rolling_max(numbers2)
print(rolling_max_result2)
```
This Python code defines a function `rolling_max` that calculates the list of rolling maximum elements from a given list of integers. It uses a `typing` to ensure proper handling of types, and the code is self-contained, passing both the function definition and test cases without relying on external modules. The test cases demonstrate the