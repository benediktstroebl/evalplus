```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This Python function, `remove_duplicates(numbers: List[int]) -> List[int]`, is designed to remove duplicate elements from a list of integers and return a new list of unique integers. The function uses a set to keep track of the seen integers, and then iterates through the input list, appending elements to the list if they haven't been seen before. The function ensures that only elements that have not been encountered before are added to the result list. 

In essence, this function facilitates the creation of lists with distinct elements, eliminating any duplicate occurrences.