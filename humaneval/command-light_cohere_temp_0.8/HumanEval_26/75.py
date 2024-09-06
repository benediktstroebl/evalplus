```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only theally in the input list.
    """
    list comprehension and set difference
    """
    new_list = []
    for num in numbers:
        if num != num.count():
            new_list.append(num)
    return new_list
```

This Python function, remove_duplicates, takes a list of integers as input and creates a new list without any duplicate integers. The function uses a list comprehension and set difference to achieve this.