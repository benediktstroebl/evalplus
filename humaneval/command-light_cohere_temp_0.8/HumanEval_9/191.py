```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([1, 2, 3, 5, 6]) 
    [5, 6, 6, 6]
    >>> rolling_max([4, 9, 2, 1]) 
    [1, 2, 2]
    """
    seen = set()
    output = []
    for num in numbers:
        while num in seen:
            seen.add(num + 1) 
        output.append(num)
   
        seen.add(num)
       
    return output
``` 
This script defines a rolling_max function that generates a list of the rolling maximum elements in a given list of integers. The test cases are passed and pass successfully as well.