```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers.
    """
    elements: List[int],  # Input list of integers
    duplicates: Set()  # To store duplicate values
    new_list: List[int]  # To store unique elements
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)  # Add the number to duplicates set
            new_list.append(num)  # Add the number to the new list
    return new_list
```