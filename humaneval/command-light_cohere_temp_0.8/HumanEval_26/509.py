```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate integers from the input list.
    Args: 
        numbers (List[int]): Input list of integers
    Returns: 
        List[int]: List of unique integers
    """
    numbers_set = set(numbers)
    return [x for x in numbers if x not in numbers_set]
``` 
This Python function called remove_duplicates takes a list of integers as input and returns a new list with all the unique integers from the original list. 

To test this function, we can pass a sample list of integers, such as [1, 2, 3, 2, 4], and the function will return the list [1, 3, 4], which are the unique integers. 
The function utilizes the set data structure to remove duplicates and then filters the list to only contain unique elements.