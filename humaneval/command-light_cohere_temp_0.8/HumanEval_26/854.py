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
This code implements a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers. The function uses a set data structure to keep track of seen numbers and a new list to store the result. The main idea is to loop through the input list, and for each number, check if it's already in the set. If it's not, it's added to the set and the new list. Then, the function returns the result list as its output.