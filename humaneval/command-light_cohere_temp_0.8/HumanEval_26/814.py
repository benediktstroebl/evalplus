```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps the exact duplicates as the original input.
    """
    Each element is only present once in the output list.
    """
    elements: List[int]
    return: List[int]
    """
    seen = {}  # dictionary to keep track of seen elements
    return [x for x in numbers if x not in seen and x not in numbers[0]] and seen.  # necessary to maintain correct behaviour with duplicate inputs.