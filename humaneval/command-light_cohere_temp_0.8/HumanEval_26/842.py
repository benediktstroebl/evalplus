```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    set_numbers = set()
    # Loop through the input list to populate the set
    for num in numbers:
        set_numbers.add(num)
    # Convert the set to a list of unique elements
    return list(set_numbers)
``` 
This function, remove_duplicates, takes a list of integers as input and returns a new list with all unique integers from the original list. The function uses the straightforwardly by converting the input set of integers into a set, and then back into a list of unique elements.