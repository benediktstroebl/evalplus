```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from the list of integers.
    Input: numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4] 
    """
    seen = {} 
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    return result
``` 
This function, remove_duplicates, takes a list of integers as input and creates a new list that contains only the integers that have appeared at most once. It uses a that for each integer in the input list, it checks if the integer is already in the seen dictionary (which keeps track of the integers we've encountered so far). 

If it's not there, it means this number has occurred at least once before, so it gets added to the result list and the seen dictionary. 

Finally, the function returns the list of integers without duplicates.