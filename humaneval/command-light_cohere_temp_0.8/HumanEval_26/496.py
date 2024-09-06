```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [list of unique integers
    """

    numbers = [1, 2, 3, 2, 4, 1, 5]
    return list(set(numbers))
``` 
This function takes a list of integers as input and returns a new list with all the unique integers from the input list. It uses the uniqueness set to create a new set of unique integers and then convert it back to a list, which effectively removes any duplicate elements.