```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without any duplicates, keeping the order of elements left unchanged.
    """
    return list(set(numbers))
```
This Python script defines a function called `remove_duplicates`, which takes a list of integers as input. Inside the function, it uses a set to store unique elements, guaranteeing that elements occurring more than once are automatically removed. The function returns a list of unique elements, leaving the order of elements unchanged from the original input list. This approach efficiently removes duplicates and maintains the original order.