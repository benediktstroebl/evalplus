```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    """
    list of integers, unique and sorted, is returned.
    """
    numbers[1:]
    unique_numbers = list(set(numbers))
    return sorted(unique_numbers)
``` 
This function utilizes the `set` function to create a set of unique numbers from the input list, and then uses the `sorted` function to sort the set. 

It then returns the sorted list of unique numbers, effectively removing any duplicates.