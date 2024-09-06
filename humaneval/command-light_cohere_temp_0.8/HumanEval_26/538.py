```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes elements that occur more than once from a list of integers.
    """
    Set a function, the input list is passed as numbers. This function creates a necessary list of integers that are not in the list of duplicates.
    return: numbers [set(filter(lambda x: not in numbers, numbers))]
    ```