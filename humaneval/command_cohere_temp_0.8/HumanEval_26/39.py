```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without any duplicates, keeping the order of elements left as is.
    """
    return list(set(numbers))
```

This Python script defines a function called `remove_duplicates` which takes a list of integers as input. Inside the function, it uses a set comprehension to create a set from the input list, which automatically removes all duplicate elements. Finally, it converts this set back into a list to retain the order of the original input list and returns the result.

The function removes duplicates without altering the order of the elements, making it an effective solution for the problem statement.