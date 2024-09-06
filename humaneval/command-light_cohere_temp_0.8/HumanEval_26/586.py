```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Returns: list of distinct elements.
    """
    kept order all elements left as in the input"""
    result = []
    for num in numbers:
        if num > 0 and num not in result:
            result.append(num)
    return result
``` 
This function utilizes a loop to iterate through the input list of integers. It checks if the duplicates are present and appends them to the result list. 

The type hint in the function signature also specifies that the input list must have integer elements.