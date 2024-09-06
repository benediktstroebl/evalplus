Here is a self-contained Python function that removes duplicates from a list of integers:
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

This function takes a list of integers as input and returns a new list with no duplicates. The function uses a set to keep track of numbers that have already been seen and removes any duplicate numbers from the input list. The function then returns the unique elements in the list. 

This script is self-contained and does not require any external functions or modules.