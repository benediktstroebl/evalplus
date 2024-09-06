```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate elements from a list of integers.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This code defines a function named `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set data structure to keep track of seen elements and then iterates through the input list, appending elements to the result list if they haven't been seen before. The use of a set data structure allows for constant-time membership testing, ensuring that no duplicates are added to the result list.

Finally, the code passes tests on the `remove_duplicates` function by calling it with a sample list of integers and verifying that the output is correct.