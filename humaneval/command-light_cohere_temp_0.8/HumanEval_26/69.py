```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and not in numbers[:seen.count()]]
    report([1, 2, 3, 2, 4])
``` 
The code defines a function remove_duplicates that takes a list of integers as input and returns a new list with all distinct integers from the input list. The function uses a set to keep track of integers that have already been seen and a list comprehension to filter out all elements from the input list that are not in the seen set and are not in the input list already. The function then returns the add all of the above elements to the result list.