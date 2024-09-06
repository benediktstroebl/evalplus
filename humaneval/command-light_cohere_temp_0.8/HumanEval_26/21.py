```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers and return the new list.
    Input:
        List[int] with duplicates 
    Output: List[int] with all duplicates removed.
    """
    test: 
    Test 1
    [1, 2, 3, 2] 
    Test 2
    [1, 2, 3, 4] 
    Test 3
    [1, 2, 3, 5] 
    Test 4
    [1, 2, 3] 
    should return: [1, 2, 3]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
The function uses a set to keep track of duplicate numbers and a list to store the numbers that have been seen before. The function then iterates through the input list, checking if each number is already in the set. If it is not, it has not been seen before and is added to the list and set.