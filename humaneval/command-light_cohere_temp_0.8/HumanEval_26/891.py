```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    Remove elements that occur more than once from a list of integers.
    Input: numbers
    Output: List[int] without duplicates
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This function, `remove_duplicates`, takes a list of integers as input and returns a new list with all integers from the input list except those that have already been added to the `seen` set. The function uses a set to keep track of the unique integers encountered so far. It iterates through the a loop through the input list, it checks if each integer is already in the set. If it's not, it adds it to both the result list and the set. This ensures that the integers are only added to the output list if they are not duplicates.