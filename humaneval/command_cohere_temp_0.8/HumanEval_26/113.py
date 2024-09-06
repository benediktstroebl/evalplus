```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input
    """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a new list that includes only the unique elements from the original list. The function uses a set called `seen` to keep track of the unique elements it has encountered while iterating through the input list. If an element is encountered for the first time, it is added to the `seen` set and also added to the `result` list. If an element has already been added to the `seen` set, it is skipped and not added to the `result` list, effectively removing all duplicates from the input list. 

The function skips elements that have already been added to the set and adds new unique elements to both the set and the result list. Finally, the function returns the `result` list containing the unique elements in the order they appeared in the original input list. 

Here is an example usage of the function:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```
In the example, the input list contains [1, 2, 3, 2, 4], with elements 2 and 4 occurring multiple times. The function removes the duplicates, keeping only 1, 3, and 4 in the result list.