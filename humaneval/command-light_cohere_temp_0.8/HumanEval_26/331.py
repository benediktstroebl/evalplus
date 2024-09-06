```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This function, `remove_duplicates`, takes a list of integers as input and returns a new list that contains only the integers that have not yet been seen before. The function uses a set to keep track of the seen integers and a new list to store the unique integers. The loop iterates through each number in the input list, and if the number is not in the set, it is added to the set and the number is added to the result list.