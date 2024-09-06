```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
# [1, 3, 4]
``` 
This Python function called `remove_duplicates` takes a list of integers as an argument and returns a new list that contains only the unique integers from the input list. The function uses a set to keep track of the seen integers and a new list to hold the results of the filtering process.