```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x > numbers[numbers.count(max)]
```
This self-contained function, rolling_max, takes a list of integers as input and returns a list of integers with the largest elements from that list. The list is generated as it iterates through the input list and uses the built-in function count(max) to find the largest element. The list is created using a list comprehension and the conditional statement.