```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: unique elements from the same set.
    """
    note that duplicates are not removed if they are the same integer.
    """
    for num in numbers:
        if num not in unique_set:
            unique_set.add(num)
    else:
            print(f" duplicate {num} found and removed" , end = "\n")
    return unique_set
```
This function takes a list of integers as input and returns a new list with all unique integers. It uses a unique set data structure to keep track of all unique integers and checks if each number in the input list is already present in the set. 

The output is printed on the screen to indicate the removal of duplicates. The new list with all unique elements is then returned.