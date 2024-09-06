```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from a list of integers.
   
    Input:
        numbers (List[int]) - List of integers to be processed.
    Output:
    List[int] without duplicates.
    """

Test case:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = set(numbers)  # Convert input list into a set
    return list(numbers)  # Convert set back to a list
```