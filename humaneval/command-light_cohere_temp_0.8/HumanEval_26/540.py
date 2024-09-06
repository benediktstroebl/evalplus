```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list of unique elements.
    """
    case:
    input:
    [1, 2, 3, 2, 4]
    output:
    [1, 3, 4]
    """
    return set(numbers) - set(numbers[: len(numbers) - 1])
``` 
This function uses the Python 'set' function to remove the duplicates and then subtracts the duplicates based on the previous element in the list.