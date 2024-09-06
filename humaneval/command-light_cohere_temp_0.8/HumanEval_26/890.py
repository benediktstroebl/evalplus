```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [set of numbers without duplicates, in any order
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all integers from the input list, but only the ones that have not been seen before (i. The function uses the set to keep track of the numbers that have been seen before, and a new list is built by appending the remaining integers. 

In each iteration, it checks if the current number is not in the seen set. If it's not, it's added to the seen set, and then added to the result list.