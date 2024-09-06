```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    """
    set(numbers) # Convert the list to set
    return [x for x in numbers if x not in set]
```
This function takes a list of integers as input and returns a new list with all unique integers from the original list. It achieves this by first converting the list into a set, and then uses a list comprehension to filter out all elements that are present in the set but not in the input list. 

This function is a self-contained, as it does not rely on any other functions or modules, and can be easily copied and used elsewhere without requiring additional dependencies.