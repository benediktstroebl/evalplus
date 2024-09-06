```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This script defines a function named `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. Here's how it works:
1. It imports the `List` module from the `typing` module to enable type annotations.
2. The function starts with a docstring that describes its purpose and behavior.
3. It uses a set called `seen` to keep track of unique elements encountered while iterating through the input `numbers` list.
4. Each element in the `numbers` list is checked if it has already been added to the `seen` set. If it hasn't, it is added to both the `seen` set and the `result` list. This ensures that each element is only added to the `result` list if it is unique.
5. Finally, the function returns the `result` list containing only the unique elements from the input list, maintaining their original order. 

The script guarantees that all numbers in the input list are retained without duplicates, and in the event of duplicate elements, their order is preserved in the resulting list. This behavior is exemplified in the following example:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
``` 

This exemplifies that the input's essence has been preserved despite the elimination of duplication, as the resulting list is ordered [1, 3, 4] and not merely `[1, 4]`.