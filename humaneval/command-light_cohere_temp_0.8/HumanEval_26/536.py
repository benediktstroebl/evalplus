```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the unbeaten elements.
    """ Return the personally tested code."""
    # Initialize Set to hold unique elements.
    seen = set()
    element = numbers[0]
    seen = [element]
    for num in numbers[1:]:
        if num == element:
            continue
        seen.append(num)
        seen.add(seen)
        seen
        return seen
``` 
This function, remove_duplicates, removes duplicate elements from a list of integers. It does this by using a set to hold unique elements and iterates through the list. The set is used to check if any elements are duplicates, and the list is used to store unbeaten elements.