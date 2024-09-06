```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from a list of integers.
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
This Python function, `remove_duplicates`, takes a list of integers as input and removes all duplicate elements. It achieves this by using a dictionary `seen` to keep track of elements that have been seen before and then iterates through the input list, appending elements to `result` only if they have not been seen before. The function returns a result, which is a list containing unique integers from the input list.