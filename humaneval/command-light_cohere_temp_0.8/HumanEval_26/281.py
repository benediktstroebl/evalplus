```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    uniq_set = set()
    result = []
    # Loop through the input list and add numbers to the set
    for num in numbers:
        uniq_set.add(num)
    # Once a number has been added once to the set, add it to the result list
    while num in uniq_set:
        uniq_set.remove(num)
    result.append(num)
return result
```
The function `remove_duplicates` takes a list of integers as input and returns a new list with all unique integers. The function uses a set data structure to keep track of the unique integers and removes any duplicate elements from the input list.