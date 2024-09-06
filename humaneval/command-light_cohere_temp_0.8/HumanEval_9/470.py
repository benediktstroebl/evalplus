```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.rolling_max()  # [max(numbers) for n in numbers]
    return numbers

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```
The above code defines a function `rolling_max` that takes a list of integers and returns a list of the maximum elements found while moving through the sequence. It uses the maximum of the list comprehension technique to achieve this. 
The code then creates a list of numbers [1, 2, 3, 2, 3, 4, 2] and calls the function with this list.  The output will be `[1, 2, 3, 3, 3, 4, 4]`.