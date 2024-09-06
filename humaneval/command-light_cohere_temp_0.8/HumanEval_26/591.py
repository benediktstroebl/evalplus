```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
``` 
This function, `remove_duplicates()`, takes a list of integers as input and removes all elements that appear more than once in the list, keeping only the first occurrence. 

The function uses a `set` to keep track of the elements that have already been seen, and then iterates through the input list. It adds each number to the `seen` set and appends it to the `result` list. Finally, it returns the list of unique integers from the `result` list.