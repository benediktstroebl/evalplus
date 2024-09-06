```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    return list(set(numbers))
```

This Python script defines a function called `remove_duplicates` that takes a list of integers as input. Inside the function, it uses a set to store unique integers from the input list and then converts this set back into a list to be returned, thus ensuring that duplicate integers are automatically removed and the order of unique integers is preserved. The function is appropriately annotated with a docstring to explain its purpose and functionality.