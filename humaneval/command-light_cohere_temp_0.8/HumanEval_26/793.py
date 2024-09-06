Here is a Python script with a self-contained function that solves the problem of removing duplicate integers from a list and passing the tests:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once in a list of integers.
    """
    set(numbers)
    return [i for i in numbers if numbers.count(i) == 1]
```

This function takes a list of integers as input and returns a new list that contains only the unique integers. The function uses the set() to remove duplicate elements and the list comprehension to filter out only the unique elements.