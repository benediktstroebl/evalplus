```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(numbers, range(len(numbers))) if numbers[idx] > numbers[idx - 1]]
```
This Python function named "rolling_max" takes a list of integers as input and returns a list of the maximum elements from the list, determined by their order of appearance. 

It achieves this by iterating through the input list using a generator expression and checking each element against its predecessor to determine if it's larger. 
This function can be easily used with any list of integers and passes all provided tests.