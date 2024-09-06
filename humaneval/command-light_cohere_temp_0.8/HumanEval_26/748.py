```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers.
    : Returns a
    list of integers where duplicate elements are to be removed.
    """
    input: List[int], returns: List[int]
    """
    # Initialize set to keep track of duplicate elements
    duplicates = set()
    result = []
    for num in numbers:
        if num not in duplicates:
            result.append(num)
            duplicates.append(num)
    return result
``` 
This function uses the Python set module to keep track of duplicate elements and removes them. The function iterates through the elements in the input list, and if an element is not in the set of duplicate elements, it is added to the result list.