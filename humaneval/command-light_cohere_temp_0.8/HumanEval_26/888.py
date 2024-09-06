```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Keep only the cores elements of the input.
    return [unique elements left as in the input list]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return list(result)
    return result
numbers = [1, 2, 3, 2, 4, 2, 3, 4]
print(remove_duplicates(numbers))
``` 
This solution uses the set data structure to keep track of the unique elements encountered in the input list. The solution iterates through the elements of the list and adds them to the result list only if they are not in the set.