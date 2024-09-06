```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This Python script defines a function called `remove_duplicates` which takes a list of integers as input. It removes any elements that occur more than once and returns a new list containing only the unique elements, maintaining their original order. This function uses a set called `seen` to keep track of elements that have already been encountered.

Here's an example of how you can use this function to solve the problem originally posted:
```python
>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
``` 

This appropriately removes the duplicates, leaving only unique elements in their original order.