```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(sorted(numbers))  # sorts the list
    return [x for x in numbers if x == numbers[-1]]  # finds the maximum element in the last element of the sorted list
x = [10,20,30,40,50,60]
rolling_max(x) # expected output: [50, 60]
 ```