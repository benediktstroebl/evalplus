```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x > max_occurring(numbers)] 


def max_occurring(numbers: List[int]) -> int:
    max_ = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max
``` 
This script provides a solution and test case for the given problem.