```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from a list of integers and return the unique list.
    """
   
    list of integers are already unique: [1, 2, 3, 4, 5]
    """
    # remove duplicates using a set to keep only unique elements
    duplicates = set(numbers)
    return list(duplicates)
``` 
This function uses the set data structure to keep track of the unique integers, then converts it back to a list.