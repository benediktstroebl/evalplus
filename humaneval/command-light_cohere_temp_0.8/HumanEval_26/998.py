```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list and return the unique elements in a new list.
    """
    `numbers` is a list of integers and you want to remove duplicate elements.
    duplicates = {x_key for key, value in numbers. duplicates for value in numbers} 
    numbers = list(set(numbers.difference(duplicates)))
    return numbers
``` 

This function uses the `set` and `difference` methods to remove duplicates from a list of integers. The resulting list contains only the unique elements.